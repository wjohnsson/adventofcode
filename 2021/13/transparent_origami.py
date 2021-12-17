import numpy as np
from operator import itemgetter


def main():
    with open('input') as f:
        grid, folds = parse_input(f.read())

    print('Part 1:', fold_x(grid, 655).sum())  # 710
    print('Part 2:')
    print_grid(apply_folds(grid, folds))  # EPLGRULR


def parse_input(inp):
    points, folds = inp.split('\n\n')

    points = [(int(x), int(y)) for x, y in [line.split(',') for line in points.splitlines()]]

    max_x = max(points, key=itemgetter(0))[0]
    max_y = max(points, key=itemgetter(1))[1]
    grid = np.zeros((max_y + 1, max_x + 1), dtype=bool)
    for x, y in points:
        grid[y][x] = True
    return grid, folds.splitlines()


def fold_x(grid, x):
    left, right = grid[:, :x], grid[:, x + 1:]
    folded = left | np.fliplr(right)
    return folded


def fold_y(grid, y):
    up, down = grid[:y, :], grid[y + 1:, :]
    folded = up | np.flipud(down)
    return folded


def print_grid(grid):
    to_string = {True: '■', False: '·'}
    for row in np.vectorize(to_string.get)(grid):
        print(''.join(row))


def apply_folds(grid, folds):
    for fold in folds:
        parts = fold.split('=')

        axis = parts[0][-1]
        coord = int(parts[1])

        if axis == 'x':
            grid = fold_x(grid, coord)
        else:
            grid = fold_y(grid, coord)
    return grid


if __name__ == '__main__':
    main()
