import re
from functools import reduce
from operator import mul
from typing import DefaultDict, List, Tuple
from collections import defaultdict

grid = [line.strip() for line in open('input').readlines()]
max_x = len(grid[0]) - 1
max_y = len(grid) - 1
offsets = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]

# Connects a gear at a specific point to a list of adjacent numbers
gears: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)


def main():
    print('Part 1', sum(numbers_adjacent_to_symbols()))
    find_gears()
    print('Part 2', sum(gear_ratios()))


def numbers_adjacent_to_symbols():
    numbers = []
    for y, line in enumerate(grid):
        for number in re.finditer(r'\d+', line):
            if any(True for x, y in adjacent_positions(y, number) if re.match(r'[^0-9.]', grid[y][x])):
                numbers.append(int(number.group()))
    return numbers


def is_within_bounds(x, y):
    return 0 <= x <= max_x and 0 <= y <= max_y


def adjacent_positions(y, number: re.Match):
    positions = set()
    for x in range(number.start(), number.end()):
        for dx, dy in offsets:
            pos = (x + dx, y + dy)
            if is_within_bounds(*pos):
                positions.add(pos)
    return positions


def find_gears():
    for y, line in enumerate(grid):
        for number in re.finditer(r'\d+', line):
            connect_number_with_gears(y, number)


def gear_ratios():
    ratios = []
    for adjacent_numbers in filter(lambda nums: len(nums) >= 2, gears.values()):
        ratios.append(reduce(mul, adjacent_numbers))
    return ratios


def connect_number_with_gears(y, number: re.Match):
    for x, y in adjacent_positions(y, number):
        if grid[y][x] == '*':
            gears[(x, y)].append(int(number.group()))


if __name__ == "__main__":
    main()
