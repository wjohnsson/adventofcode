import numpy as np
import re

input_lines = open("input").read().splitlines()


def binary_lights():
    grid = np.zeros((1000, 1000), dtype=bool)
    for line in input_lines:
        instr, coords = parse_instruction(line)
        x1, y1, x2, y2 = coords

        rect = grid[x1:x2 + 1, y1:y2 + 1]
        if instr == 'toggle':
            np.bitwise_not(rect, rect)
        else:
            grid[x1:x2 + 1, y1:y2 + 1] = ['off', 'on'].index(instr)
    return grid


def integer_lights():
    grid = np.zeros((1000, 1000), dtype=int)
    for line in input_lines:
        instr, coords = parse_instruction(line)
        x1, y1, x2, y2 = coords

        instructions = {"on": 1, "off": -1, "toggle": 2}
        grid[x1:x2 + 1, y1:y2 + 1] += instructions[instr]
        grid[grid < 0] = 0
    return grid


def parse_instruction(instruction):
    regex = r"(toggle|off|on) (\d+),(\d+) through (\d+),(\d+)"
    instr, *coords = re.findall(regex, instruction).pop()
    return instr, map(int, coords)


print("Part 1:", binary_lights().sum())  # 377891
print("Part 2:", integer_lights().sum())  # 14110788
