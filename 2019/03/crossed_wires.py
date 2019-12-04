from itertools import repeat

# Quick and dirty solution, lots of brute force and copy paste ¯\_(ツ)_/¯

input_lines = open("input.txt").readlines()


def parse_input(line_no):
    return [(trace[0], int(trace[1:])) for trace in
            input_lines[line_no].split(",")]


def visited_points(wire):
    points = set()
    # Relative distance from central port
    x, y = 0, 0
    for direction, length in wire:
        if direction == 'U':
            points.update(zip(repeat(x), range(y + 1, y + length + 1)))
            y += length
        elif direction == 'D':
            points.update(zip(repeat(x), range(y - 1, y - length - 1, -1)))
            y -= length
        elif direction == 'R':
            points.update(zip(range(x + 1, x + length + 1), repeat(y)))
            x += length
        elif direction == 'L':
            points.update(zip(range(x - 1, x - length - 1, -1), repeat(y)))
            x -= length
    return points


def steps_to_intersections(wire, intersections):
    steps = dict()
    # Relative distance from central port
    x, y = 0, 0
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


def combined_steps(intersections, stepsA, stepsB):
    combined_steps = []
    for i in intersections:
        combined_steps.append(stepsA[i] + stepsB[i])
    return combined_steps


wireA = parse_input(0)
wireB = parse_input(1)

pointsA = visited_points(wireA)
pointsB = visited_points(wireB)

intersections = set.intersection(pointsA, pointsB)
print(min([abs(x) + abs(y) for x, y in intersections]))  # 1431

stepsA = steps_to_intersections(wireA, intersections)
stepsB = steps_to_intersections(wireB, intersections)

print(min(combined_steps(intersections, stepsA, stepsB)))  # 48012
