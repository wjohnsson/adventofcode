from itertools import repeat

# Beware:
#  Quick and dirty solution, lots of brute force and copy paste ¯\_(ツ)_/¯

input_lines = open("input.txt").readlines()


def parse_input(wire_no):
    """Separate direction from length in each segment of the wire"""
    return [(segment[0], int(segment[1:])) for segment in
            input_lines[wire_no].split(",")]


def visited(wire):
    """Create a list of points visited by the wire relative to the
    central port"""
    v = set()
    x, y = 0, 0  # Relative distance from central port
    for direction, length in wire:
        if direction == 'U':
            v.update(zip(repeat(x), range(y + 1, y + length + 1)))
            y += length
        elif direction == 'D':
            v.update(zip(repeat(x), range(y - 1, y - length - 1, -1)))
            y -= length
        elif direction == 'R':
            v.update(zip(range(x + 1, x + length + 1), repeat(y)))
            x += length
        elif direction == 'L':
            v.update(zip(range(x - 1, x - length - 1, -1), repeat(y)))
            x -= length
    return v


def steps_to_intersections(wire, intersections):
    """Walk along the wire and return the distance to each intersection"""
    steps = dict()
    x, y = 0, 0  # Relative distance from the central port
    steps_taken = 0
    for direction, length in wire:
        if direction == 'U':
            for i in range(1, length + 1):
                y += 1
                steps_taken += 1
                if (x, y) in intersections:
                    steps[(x, y)] = steps_taken
        elif direction == 'D':
            for i in range(1, length + 1):
                y -= 1
                steps_taken += 1
                if (x, y) in intersections:
                    steps[(x, y)] = steps_taken
        elif direction == 'R':
            for i in range(1, length + 1):
                x += 1
                steps_taken += 1
                if (x, y) in intersections:
                    steps[(x, y)] = steps_taken
        elif direction == 'L':
            for i in range(1, length + 1):
                x -= 1
                steps_taken += 1
                if (x, y) in intersections:
                    steps[(x, y)] = steps_taken
    return steps


wireA = parse_input(0)
wireB = parse_input(1)

intersections = set.intersection(visited(wireA), visited(wireB))

# Part 1
print(min([abs(x) + abs(y) for x, y in intersections]))  # 1431

stepsA = steps_to_intersections(wireA, intersections)
stepsB = steps_to_intersections(wireB, intersections)

# Part 2
print(min([stepsA[i] + stepsB[i] for i in intersections]))  # 48012
