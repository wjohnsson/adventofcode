input_lines = open("input").read().splitlines()

move = {"N": lambda x, y: x + 1j * y,
        "S": lambda x, y: x - 1j * y,
        "E": lambda x, y: x + 1 * y,
        "W": lambda x, y: x - 1 * y}

turn = {"L": lambda x, y: x * pow(1j, y),
        "R": lambda x, y: x * pow(-1j, y)}

# Part 1
pos = 0 + 0j
direction = 1  # east
for line in input_lines:
    action = line[0]
    times = int(line[1:])
    if action in "LR":
        n_rotations = times // 90
        direction = turn[action](direction, n_rotations)
    elif action == "F":
        pos += direction * times
    else:
        pos = move[action](pos, times)

manhattan_distance = abs(pos.real) + abs(pos.imag)
print(f"Part 1: {int(manhattan_distance)}")  # 962

# Part 2
s_pos = 0 + 0j  # ship position
w_pos = 10 + 1j  # waypoint position
for line in input_lines:
    action = line[0]
    times = int(line[1:])
    if action in "LR":
        n_rotations = times // 90
        w_pos = turn[action](w_pos, n_rotations)
    elif action == "F":
        s_pos += w_pos * times
    else:  # NSEW
        w_pos = move[action](w_pos, times)

manhattan_distance = abs(s_pos.real) + abs(s_pos.imag)
print(f"Part 2: {int(manhattan_distance)}")  # 56135
