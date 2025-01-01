import re
from math import prod
import numpy as np

lines = open("input").read().splitlines()
W = 101
H = 103

def parse_input():
    robots = []
    for line in lines:
        r = tuple(int(x) for x in re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line).groups())
        robots.append(r)
    return robots

def move(robot, t):
    x, y, dx, dy = robot
    return (x + dx*t) % W, (y + dy*t) % H

def safety_factor(robots, t):
    mid_x = W // 2
    mid_y = H // 2
    #q1 q2
    #q3 q4
    q1 = range(0, mid_x), range(0, mid_y)
    q2 = range(mid_x + 1, W), range(0, mid_y)
    q3 = range(0, mid_x), range(mid_y + 1, H)
    q4 = range(mid_x + 1, W), range(mid_y + 1, H)
    qs = [q1, q2, q3, q4]

    counts = [0, 0, 0, 0]
    for r in robots:
        x, y = move(r, t)
        for i, q in enumerate(qs):
            if x in q[0] and y in q[1]:
                counts[i] += 1
    return prod(counts)


def print_grid(grid):
    to_string = {True: '■', False: '·'}
    for row in np.vectorize(to_string.get)(grid > 0):
        print(''.join(row))

robots = parse_input()
print("Part 1", safety_factor(robots, 100))  # 221142636

print("Part 2")  # 7916
for t in range(10_000):
    grid = np.zeros((H, W), dtype=int)
    positions = [move(r, t) for r in robots]
    for x, y in positions:
        grid[y][x] += 1

    if np.max(grid) == 1:  # lucky assumption
        print(f"t={t}")
        print_grid(grid)
        print("\n\n")
