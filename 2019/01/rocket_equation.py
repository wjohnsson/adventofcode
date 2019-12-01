import math

input_lines = open("input.txt").readlines()


def rocket_equation(x):
    y = math.floor(x / 3) - 2
    if y > 0:
        return y + rocket_equation(y)
    return 0  # base case


# Answer part one
print(sum([math.floor(int(x) / 3) - 2 for x in input_lines]))

# Answer part two
print(sum([rocket_equation(int(x)) for x in input_lines]))
