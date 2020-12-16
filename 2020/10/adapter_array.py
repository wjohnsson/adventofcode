import networkx as nx

adapters = list(map(int, open("input").read().splitlines()))

adapters.append(0)
adapters = sorted(adapters)
adapters.append(adapters[-1] + 3)
print(*adapters)

# Part 1
diffs = []
for i in range(len(adapters) - 1):
    diffs.append(adapters[i + 1] - adapters[i])

print(f"Part 1: {diffs.count(1) * diffs.count(3)}")

# Part 2
# The problem can be modeled as a directed acyclic graph.
# Nodes are the adapters and an edge a -> b means adapter b can be connected to a.
DG = nx.DiGraph()
DG.add_nodes_from(adapters)
for i in range(len(adapters)):
    candidates = adapters[i + 1:i + 4]
    for j, c in enumerate(candidates):
        if c - adapters[i] <= 3:
            DG.add_edge(adapters[i], adapters[i + j + 1])


def paths_from(node):
    global path_count
    edges = DG[node]
    if len(edges) == 0:  # goal node has no edges
        return 1
    if node in path_count:
        return path_count[node]

    paths = 0
    for e in edges:
        paths += paths_from(e)
    path_count[node] = paths
    return paths


path_count = {}
print(f"Part 2: {paths_from(0)}")
