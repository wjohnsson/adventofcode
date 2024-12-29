from dataclasses import dataclass
from collections import namedtuple
import re

Button = namedtuple("Button", ("dx", "dy"))
Prize = namedtuple("Prize", ("x", "y"))

@dataclass
class Machine:
    A: Button
    B: Button
    prize: Prize

def digits(line):
    return tuple(map(int, re.findall(r"\d+", line)))

def parse_input(group) -> Machine:
    lines = group.splitlines()
    return Machine(
        Button(*digits(lines[0])),
        Button(*digits(lines[1])),
        Prize(*digits(lines[2])))
    
machines = [parse_input(group) for group in open("input").read().split("\n\n")]


def solve(extra=0):
    total_cost = 0
    for m in machines:
        # I first solved the system of two linear equations on paper
        b = ((m.prize.y+extra) * m.A.dx - (m.prize.x+extra) * m.A.dy) / (m.A.dx * m.B.dy - m.B.dx * m.A.dy) 
        a = ((m.prize.x+extra) - b * m.B.dx) / m.A.dx
        
        # If solution uses integers we can complete the machine with button presses
        if int(a) == a and int(b) == b:
            total_cost += int(b) + 3*int(a)
    return total_cost

print("Part 1", solve())
print("Part 2", solve(10000000000000))