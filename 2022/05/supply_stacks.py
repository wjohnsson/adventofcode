import numpy as np
import re

input_parts = open('test_input').read().split('\n\n')

rows = input_parts[0].split('\n')[:-1]
stacks = [[row[i] for i in range(1, len(row), 4)] for row in rows]
transposed = np.rot90(stacks, 3)
stacks = [list(filter(lambda s: s != ' ', stack)) for stack in transposed]

numbers = re.compile(r'\d+')
procedures = input_parts[1].rstrip().split('\n')
procedures = [list(map(int, numbers.findall(proc))) for proc in procedures]

# Part 1 & part 2
def complete_procedure(stacks, procedures, crate_mover_9000=False):
    for count, from_s, to_s in procedures:
        crates = stacks[from_s-1][-count:]
        if not crate_mover_9000:
            crates = crates[::-1]
        stacks[from_s-1] = stacks[from_s-1][:-count]
        stacks[to_s-1] = stacks[to_s-1] + crates
    return stacks

print("".join([s[-1] for s in complete_procedure(stacks.copy(), procedures)]))
print("".join([s[-1] for s in complete_procedure(stacks, procedures, crate_mover_9000=True)]))
