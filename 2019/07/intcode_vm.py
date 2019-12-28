from collections import defaultdict


def parse_instruction(instr):
    opcode = instr % 100
    param_modes = [(instr // 10 ** i) % 10 for i in range(2, 5)]
    return opcode, param_modes


def run(program, inputs):
    pc = rb = 0  # init program counter and relative base

    # defaultdict is used for memory since it will work for any given address
    mem = defaultdict(int, enumerate(program))

    # Sizes of instructions
    sizes = {
        1: 4,  # add
        2: 4,  # mul
        3: 2,  # input
        4: 2,  # output
        5: 3,  # jump-if-true
        6: 3,  # jump-if-false
        7: 4,  # less than
        8: 4,  # equals
        9: 2,  # adjust-relative-base
    }
    while True:  # run until halt
        opcode, param_modes = parse_instruction(mem[pc])

        if opcode == 99:
            return

        size = sizes[opcode]
        params = [mem[pc + i] for i in range(1, size)]

        # The folks over at Reddit are clever...
        reads = [(mem[x], x, mem[rb + x])[mode]
                 for x, mode in zip(params, param_modes)]
        writes = [(x, None, rb + x)[mode]
                  for x, mode in zip(params, param_modes)]
        pc += size
        if opcode == 1:
            mem[writes[2]] = reads[0] + reads[1]
        elif opcode == 2:
            mem[writes[2]] = reads[0] * reads[1]
        elif opcode == 3:
            mem[writes[0]] = inputs.pop(0)
        elif opcode == 4:
            yield reads[0]
        elif opcode == 5 and reads[0]:
            pc = reads[1]
        elif opcode == 6 and not reads[0]:
            pc = reads[1]
        elif opcode == 7:
            mem[writes[2]] = int(reads[0] < reads[1])
        elif opcode == 8:
            mem[writes[2]] = int(reads[0] == reads[1])
        elif opcode == 9:
            rb += reads[0]
