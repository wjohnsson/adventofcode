import numpy as np
from functools import lru_cache
from itertools import count

inp = open('input').read().splitlines()
grid = np.array([list(map(int, list(s))) for s in inp], dtype=np.uint8)

already_flashed = set()
n_flashed = 0


def step():
    global grid, already_flashed

    already_flashed = set()

    grid += 1
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y][x] > 9 and (y, x) not in already_flashed:
                flash(y, x)
    grid[grid > 9] = 0  # reset for next step


def flash(y, x):
    global grid, n_flashed, already_flashed

    already_flashed.add((y, x))  # this step
    n_flashed += 1
    for adj_y, adj_x in get_adjacent_indices(y, x):
        grid[adj_y][adj_x] += 1
        if grid[adj_y][adj_x] > 9 and (adj_y, adj_x) not in already_flashed:
            flash(adj_y, adj_x)


@lru_cache  # memoize!
def get_adjacent_indices(y, x):
    global grid
    adj = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            range_y = range(0, grid.shape[0])  # y bounds
            range_x = range(0, grid.shape[1])  # x bounds

            (adj_y, adj_x) = (y + dy, x + dx)  # adjacent cell

            if (adj_x in range_x) and (adj_y in range_y) and (dx, dy) != (0, 0):
                adj.append((adj_y, adj_x))
    return adj


for steps in count(start=1):
    before = n_flashed
    step()
    after = n_flashed
    if steps == 100:
        print('Part 1', n_flashed)  # 1741
    if after - before == grid.size:
        print('Part 2', steps)  # 440
        break
