import networkx as nx
from collections import defaultdict

inp = open('input').read().splitlines()

G = nx.Graph([s.split('-') for s in inp])


def paths(seen, node):
    global G

    if node == 'end':
        return 1

    seen.add(node)
    count = 0
    for neighbor in G.neighbors(node):
        if not (neighbor.islower() and neighbor in seen):
            count += paths(seen.copy(), neighbor)

    return count


def paths_part2(seen, node, seen_twice=False):
    global G

    if node == 'end':
        return 1

    seen[node] += 1
    if seen[node] >= 2 and node.islower():
        seen_twice = True

    count = 0
    for neighbor in G.neighbors(node):
        if neighbor == 'start':
            continue

        if not seen_twice or not (neighbor.islower() and seen[neighbor] >= 1):
            count += paths_part2(seen.copy(), neighbor, seen_twice)

    return count


print("Part 1:", paths(set(), 'start'))  # 3738
print("Part 2:", paths_part2(defaultdict(int), 'start'))  # 120506
