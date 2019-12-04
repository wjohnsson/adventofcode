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


def adjacent_count(num):
    return list(len(list(g)) for _, g in groupby(str(num)))


def first_criterion(num):
    return max(adjacent_count(num)) >= 2


def second_criterion(num):
    return 2 in adjacent_count(num)


# Part 1
print(sum(1 for p in range(lower, upper + 1) if is_ascending(p)
          and first_criterion(p)))  # 544
# Part 2
print(sum(1 for p in range(lower, upper + 1) if is_ascending(p)
          and second_criterion(p)))  # 334
