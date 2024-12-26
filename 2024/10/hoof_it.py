lines = open("input").read().splitlines()

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
heights = []
for y, line in enumerate(lines):
    heights.append([])
    for digit in line:
        heights[y].append(int(digit))
        
    
def score(heights, y, x, unique_paths=False, seen_nines = set()) -> int:
    value = heights[y][x]
    if heights[y][x] == 9:
        if unique_paths:
            return 1
        if (y, x) not in seen_nines:
            seen_nines.add((y, x))
            return 1

    total = 0
    for dy, dx in directions:
        in_bounds = (0 <= (y + dy) < len(heights)) and (0 <= (x + dx) < len(heights))
        if in_bounds and heights[y + dy][x + dx] == value + 1:
            total += score(heights, y + dy, x + dx, unique_paths, seen_nines)
    return total

total_part1 = 0
total_part2 = 0
for y in range(len(heights)):
    for x in range(len(heights[0])):
        if heights[y][x] == 0:
            total_part1 += score(heights, y, x, unique_paths=False)
            total_part2 += score(heights, y, x, unique_paths=True)

print("Part 1:", total_part1)
print("Part 2:", total_part2)
