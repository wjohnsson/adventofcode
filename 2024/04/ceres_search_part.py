import numpy as np
from typing import List
from collections import deque

lines = open("input").read().splitlines()
grid = np.array([list(line) for line in lines])

def flatten_numpy_string_list(grid):
    return [str.join('', row) for row in grid]

def count_xmas_matches(lines):
    matches_count = 0
    for line in lines:
        window = deque()
        for char in line:
            window.append(char)
            if len(window) > 4:
                window.popleft()
            if str.join('', window) in ["XMAS", "SAMX"]:
                matches_count += 1
    return matches_count

def count_pattern_matches(grid, window_shape, patterns):
    counter = 0
    window_views = np.lib.stride_tricks.sliding_window_view(grid, window_shape)
    expected_matches = np.count_nonzero(patterns[0] != '.')

    for windows in window_views:
        for window in windows:
            for pattern in patterns:
                if np.count_nonzero(window == pattern) == expected_matches:
                    counter += 1
    return counter

def spin(pattern):
    return [np.rot90(pattern, n_rotations) for n_rotations in range(4)]

def part1_patterns():
    base_diagonal = np.array([
        ['X', '.', '.', '.'],
        ['.', 'M', '.', '.'],
        ['.', '.', 'A', '.'],
        ['.', '.', '.', 'S']
    ])
    return spin(base_diagonal)

def part2_patterns():
    base_pattern = np.array([
            ['M', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'S']
        ])
    return spin(base_pattern)

rows = count_xmas_matches(lines)
transposed_lines = flatten_numpy_string_list(grid.transpose())
columns = count_xmas_matches(transposed_lines)
diagonals = count_pattern_matches(grid, (4, 4), part1_patterns())

print("Part 1: ", rows + columns + diagonals)
print("Part 2: ", count_pattern_matches(grid, (3, 3), part2_patterns()))
