import re
from itertools import chain, combinations

program = open("input").read().splitlines()

# Part 1
mask = ""
mem = dict()
for line in program:
    if "mask" in line:
        mask = line.split("= ")[1]
    else:
        adr, val = map(int, re.findall(r"(\d+)] = (\d+)", line)[0])
        val |= int(mask.replace("X", "0"), 2)  # set 1's
        val &= int(mask.replace("X", "1"), 2)  # set 0's
        mem[adr] = val

print(f"Part 1: {sum(mem.values())}")


# Part 2
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def apply_mask(mask, adr):
    addresses = []
    # First apply bitmask
    adr |= int(mask.replace("X", "0"), 2)  # set 1's

    # Get the indexes of all Xs
    xs = [i for i, bit in enumerate(mask) if bit == "X"]

    # Then apply the floating bits
    for one_bits in powerset(xs):
        address = adr
        zero_bits = set(xs) - set(one_bits)
        for i in one_bits:
            address |= (1 << (36 - 1 - i))
        for i in zero_bits:
            address &= ~(1 << (36 - 1 - i))
        addresses.append(address)
    return addresses


mask = ""
mem = dict()
for line in program:
    if "mask" in line:
        mask = line.split("= ")[1]
    else:
        adr, val = map(int, re.findall(r"(\d+)] = (\d+)", line)[0])
        for address in apply_mask(mask, adr):
            mem[address] = val

print(f"Part 2: {sum(mem.values())}")
