disk_map = open("input").read().strip()

is_file = True
mem = []
file_id = 0
for digit in map(int, disk_map):
    for j in range(digit):
        if is_file:
            mem.append(file_id)
        else:
            mem.append(None)
    if is_file:
        file_id += 1
    is_file = not is_file


pos = 0
for i in reversed(range(0, len(mem))):
    # Skip free memory
    if mem[i] == None:
        continue

    # Find next free mem
    while True:
        if mem[pos] == None:
            break
        pos += 1

    # If everything after current pos is free mem we are done
    if all((x is None for x in mem[pos + 1:])):
        break

    # Swap
    mem[pos] = mem[i]
    mem[i] = None


print("Part 1:", sum(i * file_id for i, file_id in enumerate(mem) if file_id != None))