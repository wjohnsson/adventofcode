from collections import namedtuple

input = open("input").read().split("\n\n")
Robot = namedtuple("Robot", ("x", "y"))

deltas = {"^": (0, -1),
          ">": (1, 0),
          "v": (0, 1),
          "<": (-1, 0)}

def parse_movements():
    return input[1].replace("\n", "")

def parse_grid(wide):
    grid_input = input[0]
    if wide:
        grid_input = grid_input.replace("#", "##") \
                               .replace("O", "[]") \
                               .replace(".", "..") \
                               .replace("@", "@.")
    grid = [list(line) for line in grid_input.splitlines()]
    return grid

def find_robot(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "@":
                return Robot(x, y)
    assert(False)

def gps(x, y):
    return 100 * y + x

def move_part1(grid, robot, movement):
    x, y = robot
    dx, dy = deltas[movement]

    possible = True
    while True:
        x += dx
        y += dy
        if grid[y][x] == "#":
            possible = False
            break
        elif grid[y][x] == ".":
            grid[y][x] = "O"
            break

    if possible:
        new_x, new_y = robot.x + dx, robot.y + dy
        grid[robot.y][robot.x] = "."
        grid[new_y][new_x] = "@"
        return Robot(new_x, new_y)

    return robot

def dfs(grid, pos, delta, to_move: list) -> bool:
    if pos in to_move:
        return True

    x, y = pos
    dx, dy = delta

    if grid[y][x] == ".":
        return True
    if grid[y][x] == "#":
        return False

    to_move.append(pos)
    possible = dfs(grid, (x + dx, y + dy), delta, to_move)

    if dy != 0 and possible:
        val = grid[y][x]
        if val == "]":
            possible = possible and dfs(grid, (x - 1, y), delta, to_move)
        elif val == "[":
            possible = possible and dfs(grid, (x + 1, y), delta, to_move)
        elif val != "@":
            assert(False)

    return possible

def move_part2(grid, robot, movement):
    to_move = []
    delta = deltas[movement]
    dx, dy = delta

    possible = dfs(grid, robot, deltas[movement], to_move)
    if possible:
        move_cells(grid, to_move, dx, dy)
        return Robot(robot.x + dx, robot.y + dy)

    return robot

def move_cells(grid, to_move, dx, dy):
    replaced = dict()
    for pos in to_move:
        x, y = pos

        char = grid[y][x]

        # Save what was at that position before
        before = grid[y + dy][x + dx]
        replaced[(x + dx, y + dy)] = before

        # Move this cell
        if pos in replaced:
            char = replaced[pos]
        else:
            # Replace with empty cell
            grid[y][x] = "."
        grid[y + dy][x + dx] = char

def solve(grid, robot, movements, part):
    for movement in movements:
        if part == 1:
            robot = move_part1(grid, robot, movement)
        else:
            robot = move_part2(grid, robot, movement)

    if part == 1:
        box_char = "O"
    else:
        box_char = "["
    return sum(gps(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == box_char)


grid_part1 = parse_grid(wide=False)
grid_part2 = parse_grid(wide=True)
movements = parse_movements()
print("Part 1", solve(grid_part1, find_robot(grid_part1), movements, part=1))
print("Part 2", solve(grid_part2, find_robot(grid_part2), movements, part=2))