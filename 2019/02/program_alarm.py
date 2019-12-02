# Opcodes
ADD = 1
MUL = 2
HALT = 99

input_line = open("input.txt").readline()
intcode = [int(n) for n in input_line.split(",")]


def run_intcode(code, noun, verb):
    """Run the intcode on the ship computer"""
    code[1] = noun
    code[2] = verb

    pc = 0
    while True:
        opcode = code[pc]
        if opcode == HALT:
            break

        a = code[code[pc + 1]]
        b = code[code[pc + 2]]
        output_index = code[pc + 3]

        if opcode == ADD:
            code[output_index] = a + b
        elif opcode == MUL:
            code[output_index] = a * b
        pc += 4
    return code[0]


def part_two(wanted_output):
    for noun in range(100):
        for verb in range(100):
            result = run_intcode(intcode[:], noun, verb)
            if result == wanted_output:
                return noun, verb


print(run_intcode(intcode[:], 12, 2))  # 7594644
print(part_two(19690720))  # noun: 33, verb: 76
