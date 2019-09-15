# plants.py
# solution to https://adventofcode.com/2018/day/12
#
# TODO make adding and removing empty pots more elegant in part one solution

with open("input.txt") as f:
    lines = f.readlines()
    initial_state = lines[0].split(": ")[1].strip()

    # Only include the notes that say when the plant stays.
    # For my puzzle input, this results in having to compare 8 fewer times.
    notes = [l.strip().split(" => ")[0]
             for l in lines[2:]
             if l.strip()[-1] == "#"]

# Part one
pots = list(initial_state)
zero_index = 0

for gen in range(20):
    # The four leftmost plants might yield a new plant to their left.
    if pots[0] == "#":
        new_pots = list("....")
    elif pots[1] == "#":
        new_pots = list("...")
    elif pots[2] == "#":
        new_pots = list("..")
    elif pots[3] == "#":
        new_pots = list(".")

    zero_index += len(new_pots)
    pots = new_pots + pots

    # The four rightmost plants might yield a new plant to their right.
    if pots[len(pots) - 1] == "#":
        new_pots = list("....")
    elif pots[len(pots) - 2] == "#":
        new_pots = list("...")
    elif pots[len(pots) - 3] == "#":
        new_pots = list("..")
    elif pots[len(pots) - 4] == "#":
        new_pots = list(".")
    pots += new_pots

    # indices of pots that will contain a plant next gen.
    next_gen_plants = set()

    for i in range(len(pots) - 4):
        # For every group of adjacent 5 pots
        # LLCRR
        for note in notes:
            if "".join(pots[i:i+5]) in notes:
                # The middle pot (C) will contain a plant the next generation.
                next_gen_plants.add(i + 2)

    # clear and assign new plants
    for i in range(len(pots)):
        pots[i] = "."
        if i in next_gen_plants:
            pots[i] = "#"

for i in range(len(pots)):
    s = sum([x - zero_index for x in range(len(pots)) if pots[x] == "#"])

print("Answer part one: " + str(s))
