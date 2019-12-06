# orbit_map.py
# solution to https://adventofcode.com/2019/day/6

from collections import defaultdict


input_lines = open("input.txt").readlines()
orbits = [line.strip().split(")") for line in input_lines]

tree = defaultdict(lambda: [])
graph = defaultdict(lambda: [])
for parent, node in orbits:
    tree[parent].append(node)

    graph[parent].append(node)
    graph[node].append(parent)


def total_orbits(node, level):
    s = 0
    for child in tree[node]:
        s += total_orbits(child, level + 1)
    return level + s


def find_santa(node, parent, level):
    if node == "SAN":
        print("Santa found " + str(level - 1) + " hops away!")

    for orbit in graph[node]:
        if orbit != parent:
            find_santa(orbit, node, level + 1)


# Part 1
print(total_orbits("COM", 0))

# Part 2
find_santa(graph["YOU"][0], "YOU", 0)
