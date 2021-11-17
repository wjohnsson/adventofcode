input_line = open("input").read()

n_open = input_line.count("(")
n_close = input_line.count(")")

pos, floor = 0, 0
for i, char in enumerate(input_line):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

    if floor == -1:
        pos = i + 1
        break

print("Part 1:", n_open - n_close)
print("Part 2:", pos)
