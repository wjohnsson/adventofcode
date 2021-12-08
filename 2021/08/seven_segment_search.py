import re

lines = open("input").read().splitlines()

# left hand side
lhs = [re.findall(r"\w+", line.split("|")[0]) for line in lines]
# right hand side
rhs = [re.findall(r"\w+", line.split("|")[1]) for line in lines]

# ---- Part 1 ----
rhs_easy = [list(wires for wires in entry if len(wires) in [2, 3, 4, 7]) for entry in rhs]
print("Part 1:", sum(map(len, rhs_easy)))  # 294

# ---- Part 2 ----
decoded_sum = 0
for lhs_entry, rhs_entry in zip(lhs, rhs):
    sets = [set(wires) for wires in lhs_entry]
    len_to_num = {2: 1, 3: 7, 4: 4, 7: 8}  # works for easy
    W = {}  # num to wires
    for s in sorted(sets, key=len):
        # Easy numbers
        if len(s) in len_to_num:
            W[len_to_num[len(s)]] = s

        # Hard numbers
        elif len(s) == 5:  # 2, 3 or 5
            if len(s - W[7]) == 2:
                W[3] = s
            elif len(s.union(W[4])) == 7:
                W[2] = s
            else:
                W[5] = s
        elif len(s) == 6:  # 0, 6 or 9
            if len(s - W[4]) == 2:
                W[9] = s
            elif len(s - W[5]) == 1:
                W[6] = s
            else:
                W[0] = s

    # Now we want to go from wires to num, but sets is an un-hashable type
    # so it gets a bit messy...
    N = {"".join(sorted(list(v))): str(k) for k, v in W.items()}
    hashable = ["".join(sorted(ws)) for ws in rhs_entry]

    decoded_sum += int("".join(N[ws] for ws in hashable))

print("Part 2", decoded_sum)  # 973292
