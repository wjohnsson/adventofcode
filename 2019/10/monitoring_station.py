from math import gcd as greatest_common_divisor


def visible_count(station, asteroids):
    unique = set()  # set of unique directions
    for asteroid in asteroids:
        if asteroid == station:
            continue
        dx = asteroid[0] - station[0]
        dy = asteroid[1] - station[1]
        gcd = greatest_common_divisor(dx, dy)
        unique.add((dx // gcd, dy // gcd))

    return len(unique)


def asteroid_positions(inp):
    return [(x, y) for x in range(len(inp[0])) for y in range(len(inp))
            if inp[y][x] == "#"]


input_lines = open("input.txt").read().splitlines()
asteroids = asteroid_positions(input_lines)
# Part 1
print(max([visible_count(a, asteroids) for a in asteroids]))  # 288
