import re

inp = open('input').read()
ranges = [range(int(lo), int(hi) + 1) for lo, hi in re.findall(r"(\d+)-(\d+)", inp)]

def invalid_part1():
    invalid_sum = 0
    for r in ranges:
        for n in r:
            digits = str(n)
            mid = len(digits) // 2
            if digits[:mid] == digits[mid:]:
                invalid_sum += n
    return invalid_sum

def invalid_part2():
    return sum(n for r in ranges for n in r if is_invalid_part2(n))

def is_invalid_part2(n: int) -> bool:
    """
    Slide a window of size i over the digits, where i is the length of a substring of the digits of n.
    We only need to consider all substrings up to the middle of the string, eg:
      "abcdef" -> ["a", "ab", "abc"]
      "12345" -> ["1", "12"]
    If the substring is repeated until the end of the string it invalidates n
    """
    digits = str(n)
    mid = len(digits) // 2
    substrings_until_middle = [digits[:substring_length] for substring_length in range(1, mid + 1)]
    return any(substring_is_repeated_until_end(s, digits) for s in substrings_until_middle)


def substring_is_repeated_until_end(substring, digits):
    for i in range(0, len(digits), len(substring)):
        window = digits[i:i+len(substring)]
        if window != substring:
            return False
    return True
    

print("Part 1", invalid_part1())
print("Part 2", invalid_part2())
