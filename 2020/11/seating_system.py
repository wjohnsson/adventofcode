from itertools import permutations
from copy import deepcopy


def main():
    layout = list(map(list, (open("input").read().splitlines())))

    empty = set()
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            if layout[row][col] == "L":
                empty.add((row, col))

    # simulate() has side effects
    initial_empty = deepcopy(empty)

    occupied = simulate(4, empty, layout, count_adjacent)
    print(f"Part 1: {occupied}")  # 2283

    occupied = simulate(5, initial_empty, layout, count_visible)
    print(f"Part 2: {occupied}")  # 2054


def simulate(rule, empty, layout, count_func):
    occupied = set()
    occupy, vacate = apply_seating_rule(rule, empty, occupied, count_func, len(layout), len(layout[0]))
    while len(occupy) != 0 or len(vacate) != 0:
        for pos in occupy:
            empty.remove(pos)
            occupied.add(pos)
        for pos in vacate:
            occupied.remove(pos)
            empty.add(pos)

        occupy, vacate = apply_seating_rule(rule, empty, occupied, count_func, len(layout), len(layout[0]))

    return len(occupied)


def apply_seating_rule(rule, empty, occupied, count_func, max_row, max_col):
    occupy = set()  # seats that should be occupied after this simulation
    vacate = set()  # seats that should be emptied
    for row, col in set.union(empty, occupied):
        count = count_func(row, col, occupied, empty, max_row, max_col)

        if (row, col) in empty and count == 0:
            occupy.add((row, col))
        elif (row, col) in occupied and count >= rule:
            vacate.add((row, col))
    return occupy, vacate


# Part 1
def count_adjacent(row, col, occupied, *_):
    count = 0
    # Check all adjacent
    for dx, dy in set(permutations([0, 1, 1, -1, -1], 2)):
        if (row + dx, col + dy) in occupied:
            count += 1
    return count


# Part 2
def count_visible(row, col, occupied, empty, max_row, max_col):
    count = 0
    for dx, dy in set(permutations([0, 1, 1, -1, -1], 2)):
        r, c = row, col
        while 0 <= r < max_row and 0 <= c < max_col:
            r += dx
            c += dy
            if (r, c) in occupied or (r, c) in empty:
                if (r, c) in occupied:
                    count += 1
                break  # seat found, either empty or occupied
    return count


if __name__ == "__main__":
    main()
