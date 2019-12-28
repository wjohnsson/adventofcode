from intcode_vm import run
from itertools import permutations


def run_amps(code, phases):
    inputs = [[phase] for phase in phases]
    inputs[0].append(0)
    amps = [run(code[:], inp) for inp in inputs]

    while True:
        for i, amp in enumerate(amps):
            try:
                signal = next(amp)
            except StopIteration:
                return signal
            inputs[(i + 1) % len(amps)].append(signal)


input_line = open("input.txt").readline()
intcode = [int(n) for n in input_line.split(",")]

# Part 1
print(max([run_amps(intcode, phases)
           for phases in permutations(range(0, 5))]))  # 914828

# Part 2
print(max([run_amps(intcode, phases)
           for phases in permutations(range(5, 10))]))  # 17956613
