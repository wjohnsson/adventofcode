from itertools import groupby

lower = 356261
upper = 846303


def first_criteria(n):
    double_digits = False
    while n:
        prev = n % 10
        n //= 10
        curr = n % 10

        if prev < curr:
            # Digits are decreasing going from left to right
            return False
        if prev == curr:
            # Two adjacent digits are the same
            double_digits = True
    return double_digits


def second_criteria(n):
    temp = n
    while n:
        prev = n % 10
        n //= 10
        curr = n % 10
        if prev < curr:
            # Digits are decreasing going from left to right
            return False

    # If we have a group of length 2 we know there's two adjacent digits
    lengths = [len(list(g)) for k, g in groupby(str(temp))]
    if 2 in lengths:
        return True


print(len([n for n in range(lower, upper + 1) if first_criteria(n)]))  # 544
print(len([n for n in range(lower, upper + 1) if second_criteria(n)]))  # 334
