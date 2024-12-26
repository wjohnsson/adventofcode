from dataclasses import dataclass

@dataclass
class MemBlock:
    pos: int
    size: int
    file_id: int


disk_map = open("input").read().strip()
is_file = True
free_mem = []
files = []
file_id = 0
pos = 0
for size in map(int, disk_map):
    if is_file:
        files.append(MemBlock(pos, size, file_id))
        file_id += 1
    else:
        free_mem.append(MemBlock(pos, size, None))
    pos += size
    is_file = not is_file


def move_file(file, block):
    file.pos = block.pos

    # Reduce size of free mem block
    block.pos += file.size
    block.size -= file.size


def valid_free_block(file):
    for block in free_mem:
        if block.pos > file.pos:
            return None
        if block.size < file.size or block.size == 0:
            continue
        return block
    return None


def checksum(files):
    total = 0
    for file in files:
        for i in range(file.pos, file.pos + file.size):
            total += i * file.file_id
    return total


for file in reversed(files):
    free_block = valid_free_block(file)
    if free_block:
        move_file(file, free_block)

print("Part 2:", checksum(files))