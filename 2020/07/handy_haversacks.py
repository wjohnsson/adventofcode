import re
import networkx as nx

# Parsing input is messy but works under the assumption that bag names are exactly two words
# A rule such as:
#   "light red bags contain 1 bright white bag, 2 muted yellow bags."
# Is parsed into a dictionary entry:
#   "light red": {"bright white": 1, "muted yellow", 2}
# And added to bags
bags = dict()
for line in open("input").read().splitlines():
    bag = line.split(" bags contain")[0]
    amounts = map(int, re.findall(r"\d+", line))
    digits_removed = map(str.strip, re.split(r"\d+", line)[1:])
    bags_removed = (re.sub(r" bags?[,.]", "", s) for s in digits_removed)
    bags[bag] = dict(zip(bags_removed, amounts))

# The rules can be modeled as a weighted and directed acyclic graph
DG = nx.DiGraph()
DG.add_nodes_from(bags.keys())
for bag, contents in bags.items():
    for inner_bag, amount in contents.items():
        DG.add_edge(bag, inner_bag, weight=int(amount))

print(f"Part 1: {len(nx.ancestors(DG, 'shiny gold'))}")  # 151


# Part 2
def bag_count(tree, node):
    count = 0
    for n, w in tree[node].items():
        weight = w["weight"]
        count += weight + weight * bag_count(tree, n)
    return count


print(f"Part 2: {bag_count(DG, 'shiny gold')}")  # 41559
