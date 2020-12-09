from itertools import combinations
from math import prod

input_lines = open("input").readlines()
er = list(map(int, input_lines))  # expense report

# Part 1
for pair in combinations(er, 2):
    if sum(pair) == 2020:
        print(f"Part 1: {prod(pair)}")  # 842016

# Part 2
for triplet in combinations(er, 3):
    if sum(triplet) == 2020:
        print(f"Part 2: {prod(triplet)}")  # 9199664
