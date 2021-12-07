xs = list(map(int, open("input").read().rstrip().split(",")))


def fuel_cost(xs, pos, constant=True):
    if constant:
        # Part 1
        return sum(abs(x - pos) for x in xs)

    # Part 2
    return sum(triangular_number(abs(x - pos)) for x in xs)


def triangular_number(n):
    return n * (n + 1) // 2


print("Part 1:", min(fuel_cost(xs, pos) for pos in range(max(xs) + 1)))  # 355521
print("Part 2:", min(fuel_cost(xs, pos, constant=False) for pos in range(max(xs) + 1)))  # 100148777
