from operator import mul

def main():
    grid, guard_pos = parse_grid()
    visited = move_guard(grid, guard_pos)
    print()
    print("Part 1:", len(visited))
    print("Part 2:", count_loops(grid, guard_pos, visited))


def parse_grid():
    lines = open("input").read().splitlines()
    grid = dict()
    guard_pos = complex()
    for row, line in enumerate(lines):  # set origin in bottom left
        for col, char in enumerate(line):
            pos = complex(col, -row)
            if char == '^':
                guard_pos = pos
            grid[pos] = char
    return grid, guard_pos


class GuardInLoop(Exception):
    pass


def move_guard(grid, guard_pos):
    direction = 1j  # up
    turn = lambda x: mul(x, -1j)  # 90 deg clockwise
    visited = set()
    while True:
        try:
            if (guard_pos, direction) in visited:
                raise GuardInLoop
            visited.add((guard_pos, direction))
            while grid[guard_pos + direction] == '#':
                direction = turn(direction)
            guard_pos += direction
        except KeyError:
            break
    return set(pos for pos, _ in visited)


def count_loops(grid, inital_guard_pos, unobstacled_visits):
    loops = 0
    # All visited nodes without obstacles are candidates
    for obstacle in unobstacled_visits:
        # Cannot place obstacle where guard is standing
        if obstacle == inital_guard_pos:
            continue

        # Place obstacle in front of a visited node and check if it creates a loop
        grid_copy = grid.copy()
        grid_copy[obstacle] = '#'
        try:
            move_guard(grid_copy, inital_guard_pos)
        except GuardInLoop:
            loops += 1
    return loops


if __name__ == "__main__":
    main()