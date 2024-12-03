import re
from itertools import dropwhile

memory = open("input").read()
mul_matches = list(re.finditer(r"mul\((\d+),(\d+)\)", memory))

def start_indexes(regex):
    return [match.start() for match in re.finditer(regex, memory)]

def get_enabled_segments():
    dos = start_indexes(r"do\(\)")
    dos.insert(0, 0)  # enable at start 
    donts = start_indexes(r"don't\(\)")

    segments = []
    for do in dos:
        next_dont = next(dropwhile(lambda dont: do > dont, donts))
        segments.append([do, next_dont])
    return segments

def run_instructions(enabled_segments):
    total = 0
    for match in mul_matches:
        is_enabled = any(True for lower, upper in enabled_segments if lower < match.start() < upper)
        if is_enabled:
            a, b =  map(int, match.groups())
            total += a * b
    return total

print("Part 1:", run_instructions([(0, len(memory) - 1)]))
print("Part 2:", run_instructions(get_enabled_segments()))