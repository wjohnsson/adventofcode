from collections import deque
from itertools import combinations

nums = list(map(int, open("input").read().splitlines()))
preamble_length = 25

# Both parts are brute forced ¯\_(ツ)_/¯
# Part 1
invalid_n = 0
prev_nums = deque(nums[:preamble_length])
for n in nums[preamble_length:]:
    pair_sums = map(sum, combinations(prev_nums, 2))
    if n not in pair_sums:
        invalid_n = n  # 88311122
        break
    prev_nums.popleft()
    prev_nums.append(n)

print(f"Part 1: {invalid_n}")  # 88311122


# Part 2
def find_range():
    global s
    for j in range(i + 1, len(nums) - 1):
        s += nums[j]
        if s == invalid_n:
            contiguous_range = nums[i:j+1]
            return min(contiguous_range) + max(contiguous_range)
        if s > invalid_n:
            return None


for i in range(len(nums)):
    s = nums[i]
    ans = find_range()
    if ans:
        print(f"Part 2: {ans}")  # 13549369
        break
