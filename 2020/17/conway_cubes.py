from itertools import permutations
from collections import defaultdict

# State
active, active_neighbors = set(), defaultdict(int)

# When applied - yields all neighbors of a given coordinate
deltas = set(permutations([0, 0, 1, 1, 1, -1, -1, -1], 3))


def main():
    global active
    # Input
    starting_state = ("..##.#.#"
                      "\n##....#."
                      "\n....####"
                      "\n#..##..."
                      "\n#..#.##."
                      "\n.#..#..."
                      "\n##...##."
                      "\n.#...#..")

    # starting_state = ".#.\n..#\n###"  # Test
    parse_input(starting_state)

    for _ in range(6):
        activate, deactivate = one_cycle()
        for pos in activate:
            active.add(pos)
            add_neighbors(1, *pos)
        for pos in deactivate:
            active.remove(pos)
            add_neighbors(-1, *pos)

    print(len(active))


def parse_input(starting_state):
    global active
    # Set top left starting state at coordinate system origin
    z = y = 0
    for line in starting_state.splitlines():
        x = 0
        for char in line:
            if char == "#":
                active.add((x, y, z))
                add_neighbors(1, x, y, z)
            x += 1
        y -= 1


def one_cycle():
    """Simulates one cycle. Returns the cells that shall be activated and deactivated before next cycle."""
    global active, active_neighbors
    activate = set()
    deactivate = set()

    for pos in active_neighbors:
        if pos in active:
            if not (2 <= active_neighbors[pos] <= 3):
                # active and not 2 or 3
                deactivate.add(pos)
        else:
            if active_neighbors[pos] == 3:
                # inactive and exactly 3
                activate.add(pos)
    return activate, deactivate


def add_neighbors(amount, x, y, z):
    global deltas, active_neighbors
    for dx, dy, dz in deltas:
        active_neighbors[x + dx, y + dy, z + dz] += amount


if __name__ == "__main__":
    main()
