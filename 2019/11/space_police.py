from intcode_vm import run
from operator import mul
from collections import defaultdict


def run_robot(code, start_color=0):
    pos = 0+0j
    direction = 1j  # up
    grid = defaultdict(int)
    grid[pos] = start_color
    turn = [lambda x: mul(x, 1j), lambda x: mul(x, -1j)]

    inp = []
    program = run(code[:], inp)
    while True:
        try:
            inp.append(grid[pos])
            grid[pos] = next(program)
            direction = turn[next(program)](direction)
            pos += direction
        except StopIteration:
            return grid


def print_grid(grid):
    min_x = int(min(grid, key=lambda z: z.real).real)
    max_x = int(max(grid, key=lambda z: z.real).real)
    min_y = int(min(grid, key=lambda z: z.imag).imag)
    max_y = int(max(grid, key=lambda z: z.imag).imag)

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            color = grid[complex(x, y)]
            if color == 0:
                print("█", end="")
            elif color == 1:
                print("░", end="")
        print()


input_line = open("input.txt").readline()
intcode = [int(n) for n in input_line.split(",")]

# Part 1
print(len(run_robot(intcode)))  # 2016

# Part 2
print_grid(run_robot(intcode, 1))  # RAPRCBPH
