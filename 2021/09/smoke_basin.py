import numpy as np
from math import prod

inp = open("input").read().splitlines()
grid = np.array([list(map(int, list(s))) for s in inp], dtype=np.uint8)

# Pad the grid wth maxint to avoid oob stuff
grid = np.pad(grid, ((1, 1), (1, 1)), constant_values=np.iinfo(grid.dtype).max)
#           N        S       E        W
deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def low_points():
    lps = []  # low points
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            point = grid[y][x]
            if all(point < grid[y + dy][x + dx] for dy, dx in deltas):
                lps.append((y, x))
    return lps


visited = set()


def size_of_basin(y, x):
    visited.add((y, x))
    size = 1
    point = grid[y][x]
    for dy, dx in deltas:
        next_point = grid[y + dy][x + dx]
        if point < next_point <= 8 and (y + dy, x + dx) not in visited:
            size += size_of_basin(y + dy, x + dx)
    return size


low_points = low_points()
print("Part 1", sum(1 + grid[point] for point in low_points))  # 558

three_largest = sorted([size_of_basin(*point) for point in low_points], reverse=True)[:3]
print("Part 2", prod(three_largest))  # 882942
