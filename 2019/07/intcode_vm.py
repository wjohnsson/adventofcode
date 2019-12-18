from queue import SimpleQueue

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

ARITY = {ADD: 3, MUL: 3, IN: 1, OUT: 1, JNZ: 2, JEZ: 2, SLT: 3, EQ: 3}


class IntcodeVM:
    def __init__(self, mem, output_vm):
        self.mem = mem
        self.pc = 0
        self.input_queue = SimpleQueue()
        self.output_vm = output_vm

    @staticmethod
    def parse_instruction(instr):
        opcode = instr % 100
        param_modes = [int(x) for x in str(instr // 100).zfill(4)]
        return opcode, param_modes

    @staticmethod
    def get_params(mem, pc, param_modes, arity):
        params = []
        for i in range(arity):
            mode = param_modes.pop()
            if mode == IMM:
                params.append(mem[pc + 1 + i])
            elif mode == POS:
                params.append(mem[mem[pc + 1 + i]])
            else:
                raise ValueError
        return params

    def next_input(self, inp):
        self.input_queue.put(inp)

    def run(self):
        """
        Run VM until halt or input queue is empty
        """
        mem = self.mem
        pc = self.pc
        while True:
            opcode, param_modes = self.parse_instruction(mem[pc])

            if opcode == HALT:
                break

            params = self.get_params(mem, pc, param_modes, ARITY[opcode])
            p3 = mem[pc + 3]  # third parameter, always positional

            if opcode == IN:
                mem[mem[pc + 1]] = self.input_queue.get()  # blocks if empty
                pc += 2
            elif opcode == OUT:
                if self.output_vm is None:
                    return params[0]
                else:
                    self.output_vm.next_input(params[0])
                pc += 2

            elif opcode == ADD:
                mem[p3] = params[0] + params[1]
                pc += 4

            elif opcode == MUL:
                mem[p3] = params[0] * params[1]
                pc += 4

            elif opcode == JNZ:
                if params[0] != 0:
                    pc = params[1]
                else:
                    pc += 3

            elif opcode == JEZ:
                if params[0] == 0:
                    pc = params[1]
                else:
                    pc += 3

            elif opcode == SLT:
                if params[0] < params[1]:
                    mem[p3] = 1
                else:
                    mem[p3] = 0
                pc += 4

            elif opcode == EQ:
                if params[0] == params[1]:
                    mem[p3] = 1
                else:
                    mem[p3] = 0
                pc += 4

            else:
                print("unknown opcode " + str(opcode) + " exiting...")
                break
