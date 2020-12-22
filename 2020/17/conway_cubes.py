from itertools import product
from collections import defaultdict

# State
active, active_neighbors = set(), defaultdict(int)

# When applied - yields all neighbors of a given coordinate
deltas = set()


def main():
    global active, active_neighbors, deltas
    # Input
    starting_state = ("..##.#.#"
                      "\n##....#."
                      "\n....####"
                      "\n#..##..."
                      "\n#..#.##."
                      "\n.#..#..."
                      "\n##...##."
                      "\n.#...#..")

    # Test
    # starting_state = ".#.\n..#\n###"

    # ---- Part 1 ----
    # 3D
    deltas = get_deltas(3)
    parse_input(starting_state, 3)

    simulate(6)
    print(f"Part 1: {len(active)}")  # 202

    # ---- Part 2 ----
    # 4D
    active, active_neighbors = set(), defaultdict(int)  # reset state
    deltas = get_deltas(4)
    parse_input(starting_state, 4)

    simulate(6)
    print(f"Part 2: {len(active)}")  # 2028


def parse_input(starting_state, dimensions):
    global active
    # Set top left starting state at coordinate system origin
    pos = [0] * dimensions
    for line in starting_state.splitlines():
        pos[0] = 0
        for char in line:
            if char == "#":
                active.add(tuple(pos))
                add_neighbors(1, tuple(pos))
            pos[0] += 1
        pos[1] -= 1


def get_deltas(dimensions):
    ds = set(product([0, 1, -1], repeat=dimensions))
    ds.remove(tuple([0] * dimensions))
    assert len(ds) == 3 ** dimensions - 1  # https://oeis.org/A024023
    return ds


def simulate(steps):
    global active

    for _ in range(steps):
        activate, deactivate = one_cycle()
        for pos in activate:
            active.add(pos)
            add_neighbors(1, pos)
        for pos in deactivate:
            active.remove(pos)
            add_neighbors(-1, pos)


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


def add_neighbors(amount, pos):
    global deltas, active_neighbors
    for delta in deltas:
        # neighbor_pos = [pos.x + dx, pos.y + dy, ...]
        neighbor_pos = tuple([pos[i] + delta[i] for i in range(len(pos))])
        active_neighbors[neighbor_pos] += amount


if __name__ == "__main__":
    main()
