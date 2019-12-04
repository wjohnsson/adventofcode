from itertools import groupby

lower = 356261
upper = 846303


def is_ascending(num):
    while num:
        prev = num % 10
        num //= 10
        curr = num % 10

        if prev < curr:
            # Digits are decreasing going from left to right
            return False
    return True


def first_criteria(n):
    while n:
        prev = n % 10
        n //= 10
        curr = n % 10

        if prev == curr:
            # Two adjacent digits are the same
            return True
    return False


def second_criteria(n):
    s = str(n)
    # If we have a group of length 2 we know there's two adjacent digits
    return any([len(list(g)) == 2 for _, g in groupby(s)])


print()
print(len([n for n in range(lower, upper + 1) if is_ascending(n) and first_criteria(n)]))  # 544
print(len([n for n in range(lower, upper + 1) if is_ascending(n) and second_criteria(n)]))  # 334
