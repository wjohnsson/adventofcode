from itertools import combinations
from collections import defaultdict, namedtuple

Point = namedtuple("Pos", ["x", "y"])
Vector = namedtuple("Vec", ["dx", "dy"])
lines = open("input").read().splitlines()

max_y = len(lines) - 1
max_x = len(lines[0]) - 1

antennaes = defaultdict(list)
for y, line in enumerate(reversed(lines)):  # origin at bottom left
    for x, char in enumerate(line):
        if char != ".":
            antennaes[char].append(Point(x, y))

def in_bounds(p):
    return 0 <= p.x <= max_x and 0 <= p.y <= max_y

def points_on_line(start, v, part2):
    points = set()
    p = start
    while True:
        p = Point(p.x + v.dx, p.y + v.dy)

        if not in_bounds(p):
            return points

        points.add(p)

        if not part2:
            return points

def solve(part2):
    antinodes = set()
    for positions in antennaes.values():
        pairs = combinations(positions, 2)
        for a, b in pairs:
            Vab = Vector(b.x - a.x, b.y - a.y)  # vector pointing from a to b
            Vba = Vector(-Vab.dx, -Vab.dy)      # vector pointing from b to a

            if part2:
                antinodes.add(a)
                antinodes.add(b)
            antinodes = antinodes.union(points_on_line(b, Vab, part2))
            antinodes = antinodes.union(points_on_line(a, Vba, part2))

    return len(antinodes)

print("Part 1:", solve(part2=False))
print("Part 2:", solve(part2=True))