from intcode_vm import IntcodeVM
from itertools import permutations

input_line = open("input.txt").readline()
intcode = [int(n) for n in input_line.split(",")]


def run_vms(phases):
    vms = [IntcodeVM(intcode[:], None)]  # last amp
    for i in range(4):
        vms.append(IntcodeVM(intcode[:], vms[i]))
    vms.reverse()

    for i, phase in enumerate(phases):
        vms[i].next_input(phase)
    vms[0].next_input(0)

    for vm in vms[:-1]:
        vm.run()
    return vms[4].run()


# Part 1
print(max([run_vms(phases) for phases in permutations(range(0, 5))]))
