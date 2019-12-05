import operator

# Opcodes
ADD = 1
MUL = 2
IN = 3
OUT = 4
HALT = 99

# Parameter modes
POS = 0  # positional
IMM = 1  # immediate


input_line = open("input.txt").readline().strip()
intcode = [int(n) for n in input_line.split(",")]


def parse_instruction(instr):
    opcode = instr % 100
    param_modes = [int(x) for x in str(instr // 100).zfill(3)]
    return opcode, param_modes


def arith_op(mem, pc, op, param_modes):
    """Return result of applying op to the instruction parameters"""
    if param_modes.pop() == IMM:
        a = mem[pc + 1]
    else:
        a = mem[mem[pc + 1]]
    if param_modes.pop() == IMM:
        b = mem[pc + 2]
    else:
        b = mem[mem[pc + 2]]
    return op(a, b)


def run_intcode(mem):
    """Run the intcode on the ship computer"""
    pc = 0  # program counter
    while True:
        opcode, param_modes = parse_instruction(mem[pc])

        if opcode == HALT:
            break
        elif opcode == IN:
            mem[mem[pc + 1]] = 1  # we always input 1 anyways
            pc += 2
        elif opcode == OUT:
            print(mem[mem[pc + 1]])
            pc += 2
        elif opcode == ADD:
            mem[mem[pc + 3]] = arith_op(mem, pc, operator.add, param_modes)
            pc += 4
        elif opcode == MUL:
            mem[mem[pc + 3]] = arith_op(mem, pc, operator.mul, param_modes)
            pc += 4
        else:
            print("unknown opcode " + str(opcode) + " exiting...")
            break


run_intcode(intcode)  # 9654885
