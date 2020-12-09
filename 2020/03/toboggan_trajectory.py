from math import prod

m = open("input").readlines()  # map
h, w = len(m), len(m[0])  # map dimensions (height, width)


def trees_encountered(dx, dy):
    trees = x = 0
    for y in range(dy, h, dy):
        x = (x + dx) % (w - 1)

        if m[y][x] == "#":
            trees += 1
    return trees


print(f"Part 1: {trees_encountered(3, 1)}")  # 278

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_trees = [trees_encountered(dx, dy) for dx, dy in slopes]
print(f"Part 2: {prod(total_trees)}")  # 9709761600
