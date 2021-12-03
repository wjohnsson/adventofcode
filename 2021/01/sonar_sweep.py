input_lines = open("input").read().splitlines()
ms = list(map(int, input_lines))  # measurements

print("Part 1:", sum(a < b for a, b in zip(ms, ms[1:])))
# a+b+c < b+c+d if a < d
print("Part 2:", sum(a < b for a, b in zip(ms, ms[3:])))
