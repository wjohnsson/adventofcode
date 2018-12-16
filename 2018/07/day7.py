from collections import defaultdict
import heapq

# Step Q must be finished before step O can begin.
# Step Z must be finished before step G can begin.
# Step W must be finished before step V can begin.
# Step C must be finished before step X can begin.
# Step O must be finished before step E can begin.


class Graph:
    def __init__(self):
        # A dictionary of steps where a key is a label and the value is a list
        # of elements it allows completion of.
        self.nodes = defaultdict(list)

    def add_edge(self, label, allows):
        self.nodes[label].append(allows)

    def topological_sort_util(self, visited):

    def topological_sort(self, node):
        edge_queue = []

        for edge in self.nodes[node]:
            heapq.heappush(edge_queue, edge)

        while len(edge_queue) > 0:
            self.toplogical_sort(self.nodes[edge_queue.pop()])

        return node


g = Graph()
lines = open("test.txt").readlines()

for line in lines:
    node, edge = line.split()[1], line.split()[7]
    g.add_edge(node, edge)

g.step_order(lines[0].split()[1])
