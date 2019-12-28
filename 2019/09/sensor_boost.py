# sensor_boost.py
# solution to https://adventofcode.com/2019/day/9

from intcode_vm import run

program = [int(n) for n in open("input.txt").readline().split(",")]

# Part 1
print(list(run(program, [1])))  # [3906448201]

# Part 2
print(list(run(program, [2])))  # [59785]
