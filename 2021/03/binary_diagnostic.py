import numpy as np
from collections import Counter

input_lines = open("input").read().splitlines()
nums = np.array(list(map(list, input_lines)))


def part1():
    most_common, least_common = "", ""
    for row in nums.T:
        (d0, _), (d1, _) = Counter(row).most_common()
        most_common += d0
        least_common += d1

    gamma = int(most_common, 2)
    epsilon = int(least_common, 2)
    return gamma * epsilon


def part2():
    oxygen = nums[:]
    co2 = nums[:]
    for col in range(nums.shape[1]):
        # Stop when there is only one left
        if len(oxygen) != 1:
            (most_common, c0), (_, c1) = Counter(oxygen[:, col]).most_common()
            if c0 == c1:
                most_common = '1'
            oxygen = oxygen[oxygen[:, col] == most_common]

        if len(co2) != 1:
            (_, c0), (least_common, c1) = Counter(co2[:, col]).most_common()
            if c0 == c1:
                least_common = '0'
            co2 = co2[co2[:, col] == least_common]

    oxygen_rating = int("".join(oxygen.flatten()), 2)
    co2_rating = int("".join(co2.flatten()), 2)

    return oxygen_rating * co2_rating


print("Part 1:", part1())
print("Part 2:", part2())
