input_line = open("input").read()
deltas = {"^": 1j,
          ">": 1,
          "v": -1j,
          "<": -1}

# Part 1
houses = set()

pos = 0 + 0j
for char in input_line:
    pos += deltas[char]
    houses.add(pos)

print("Part 1:", len(houses))


# Reset for part 2
houses = set()

santa_pos = 0 + 0j
robot_pos = 0 + 0j
houses.add(0 + 0j)

pairs = zip(input_line[::2], input_line[1::2])
for santa_move, robot_move in pairs:
    santa_pos += deltas[santa_move]
    houses.add(santa_pos)

    robot_pos += deltas[robot_move]
    houses.add(robot_pos)

print("Part 2:", len(houses))
