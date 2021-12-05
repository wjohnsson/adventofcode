import re
import numpy as np

input_lines = open("input").read().splitlines()
lines = [re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", s)[0] for s in input_lines]
lines = [tuple(map(int, line)) for line in lines]

max_x = np.max(np.array([(x1, x2) for x1, _, x2, _ in lines]).flatten())
max_y = np.max(np.array([(y1, y2) for _, y1, _, y2 in lines]).flatten())

overlaps = np.zeros((max_y + 1, max_x + 1), dtype=np.int)

# ---- Part 1 ----
# Horizontal and vertical line segments
hv = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2 or y1 == y2]
for x1, y1, x2, y2 in hv:
    # For slicing
    max_x, min_x = max(x1, x2), min(x1, x2)
    max_y, min_y = max(y1, y2), min(y1, y2)
    # numpy has in place modification of slices
    overlaps[min_y:max_y + 1, min_x:max_x + 1] += 1

print("Part 1:", overlaps[overlaps >= 2].size)  # 5442

# ---- Part 2 ----
# Diagonal line segments
diags = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if not (x1 == x2 or y1 == y2)]
for x1, y1, x2, y2 in diags:
    n_points = abs(x1 - x2) + 1
    points = np.linspace((x1, y1), (x2, y2), n_points, dtype=np.int)
    for x, y in points:
        overlaps[y][x] += 1

print("Part 2:", overlaps[overlaps >= 2].size)  # 19571
