# Instruction set
ADD = 1    # Addition
MUL = 2    # Multiplication
IN = 3     # Get user input
OUT = 4    # Print
JNZ = 5    # Jump if Non-Zero
JEZ = 6    # Jump if Zero
SLT = 7    # Store 1 if Less Than, 0 otherwise
EQ = 8     # Store 1 if equal, 0 otherwise
HALT = 99  # Halt program

# Parameter modes
POS = 0  # positional
IMM = 1  # immediate


def parse_instruction(instr):
    opcode = instr % 100
    param_modes = [int(x) for x in str(instr // 100).zfill(3)]
    return opcode, param_modes


def get_params(mem, pc, param_modes):
    """Return two parameters using parameter modes."""
    params = []
    for i in range(2):
        mode = param_modes.pop()
        if mode == IMM:
            params.append(mem[pc + 1 + i])
        elif mode == POS:
            params.append(mem[mem[pc + 1 + i]])
        else:
            raise ValueError
    return params[0], params[1]


def run_intcode(mem, initial_input):
    """Run the intcode on the ship computer."""
    pc = 0  # program counter
    while True:
        opcode, param_modes = parse_instruction(mem[pc])

        # Welcome to If City, enjoy your stay.
        if opcode == HALT:
            break
        elif opcode == IN:
            mem[mem[pc + 1]] = initial_input
            pc += 2
        elif opcode == OUT:
            print(mem[mem[pc + 1]])
            pc += 2
        else:
            # All other operations have at least 2 params
            p1, p2 = get_params(mem, pc, param_modes)
            p3 = mem[pc + 3]  # third parameter, always positional

            if opcode == ADD:
                mem[p3] = p1 + p2
                pc += 4

            elif opcode == MUL:
                mem[p3] = p1 * p2
                pc += 4

            elif opcode == JNZ:
                if p1 != 0:
                    pc = p2
                else:
                    pc += 3

            elif opcode == JEZ:
                if p1 == 0:
                    pc = p2
                else:
                    pc += 3

            elif opcode == SLT:
                if p1 < p2:
                    mem[p3] = 1
                else:
                    mem[p3] = 0
                pc += 4

            elif opcode == EQ:
                if p1 == p2:
                    mem[p3] = 1
                else:
                    mem[p3] = 0
                pc += 4

            else:
                print("unknown opcode " + str(opcode) + " exiting...")
                break


input_line = open("input.txt").readline().strip()
intcode = [int(n) for n in input_line.split(",")]

# Part 1
run_intcode(intcode[:], 1)  # 9654885

# Part 2
run_intcode(intcode[:], 5)  # 7079459
