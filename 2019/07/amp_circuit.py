from intcode_vm import IntcodeVM
from itertools import permutations


def run_serial_amps(code, phases):
    amps = init_amps(code, phases)
    signal = 0
    for amp in amps:
        amp.next_input(signal)
        signal = amp.run()
    return signal


def run_feedback_amps(code, phases):
    amps = init_amps(code, phases)
    signal = 0
    halt = False
    while not halt:
        for amp in amps:
            amp.next_input(signal)
            try:
                signal = amp.run()
            except StopIteration:
                halt = True
    return signal


def init_amps(code, phases):
    amps = [IntcodeVM(code[:])]  # last amp
    for i in range(4):
        amps.append(IntcodeVM(intcode[:]))
    amps.reverse()

    for i, phase in enumerate(phases):
        amps[i].next_input(phase)
    return amps


input_line = open("input.txt").readline()
intcode = [int(n) for n in input_line.split(",")]

# Part 1
print(max([run_serial_amps(intcode, phases) for phases in permutations(range(0, 5))]))

# Part 2
print(max([run_feedback_amps(intcode, phases) for phases in permutations(range(5, 10))]))
