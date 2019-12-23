import math


def visible_asteroids(station, asteroids):
    visible = set()  # set of visible asteroids
    for asteroid in asteroids:
        if asteroid == station:
            continue
        dx = asteroid[0] - station[0]
        dy = asteroid[1] - station[1]
        gcd = math.gcd(dx, dy)
        visible.add((dx // gcd, dy // gcd))

    return station, visible


def asteroid_positions(inp):
    return [(x, y) for x in range(len(inp[0])) for y in range(len(inp))
            if inp[y][x] == "#"]


def fire_lazer(station, visible, asteroids):
    # Since the 200th asteroid is visible, we only need to do one rotation
    # Flip atan2 arguments to start angles from y-axis
    vaporized = [(math.atan2(dx, dy), (dx, dy)) for dx, dy in visible]

    # Use reverse sort so that smallest angles (negative) are vaporized last
    vaporized.sort(reverse=True)
    dx, dy = vaporized[200-1][1]

    # Find actual coordinate of 200th vaporized asteroid
    x, y = station[0]+dx, station[1]+dy
    while (x, y) not in asteroids:
        x, y = x+dx, y+dy

    return x*100 + y


input_lines = open("input.txt").read().splitlines()
asteroids = asteroid_positions(input_lines)
options = [visible_asteroids(a, asteroids) for a in asteroids]
best_station, visible = max(options, key=lambda x: len(x[1]))

# Part 1
print(len(visible))  # 288

# Part 2
print(fire_lazer(best_station, visible, asteroids))  # 616
