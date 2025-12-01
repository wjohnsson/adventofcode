lines = open('input').read().splitlines()

pos = 50
zeros_part1, zeros_part2 = 0, 0

for line in lines:
    direction = line[0]
    steps = int(line[1:])

    if direction == 'L':
        zeros_part2 += ((100 - pos) % 100 + steps) // 100  # convert left steps into right steps
        pos -= steps
    else:
        zeros_part2 += (pos + steps) // 100
        pos += steps

    pos %= 100
    if pos == 0:
        zeros_part1 += 1

print("Part 1", zeros_part1)
print("Part 2", zeros_part2)
