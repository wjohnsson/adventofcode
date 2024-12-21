from itertools import product
from operator import mul, add
import re

lines = open("input").read().splitlines()

def test_operator_set(operator_set, operands, target):
    running_total = operands[0]
    for i, operator in enumerate(operator_set):
        running_total = operator(running_total, operands[i + 1])
        if running_total > target:
            return False
        if running_total == target:
            return True
    return False

def solve(operators):
    sum_of_correct_lines = 0
    for line in lines:
        nums = re.findall(r"\d+", line)
        target = int(nums[0])
        operands = [int(num) for num in nums[1:]]
        for operator_set in product(operators, repeat=len(operands) - 1):
            if test_operator_set(operator_set, operands, target):
                sum_of_correct_lines += target
                break
    return sum_of_correct_lines

print("Part 1: ", solve([mul, add]))
print("Part 2: ", solve([mul, add, lambda x, y: int(str(x) + str(y))]))
