import re
from collections import Counter
from functools import cache


def main():
    global template, rules

    counts_part1 = Counter(template)
    counts_part2 = Counter(template)
    for left, right in zip(template, template[1:]):
        counts_part1 += step(left, right, 10)
        counts_part2 += step(left, right, 40)

    print('Part 1:', most_minus_least_common(counts_part1))
    print('Part 2:', most_minus_least_common(counts_part2))


def parse_input(inp):
    template = inp.split('\n\n')[0]
    rules = [re.findall(r'\w+', line) for line in inp.splitlines()[2:]]
    rules = {(char1, char2): v for (char1, char2), v in rules}
    return list(template), rules


@cache
def step(left, right, max_depth, depth=1):
    if depth > max_depth:
        return Counter()

    mid = rules[(left, right)]
    counts = Counter({mid: 1})
    counts += step(left, mid, max_depth, depth + 1)
    counts += step(mid, right, max_depth, depth + 1)
    return counts


def most_minus_least_common(counts):
    sorted_counts = Counter(counts).most_common()
    (_, most), (_, least) = sorted_counts[0], sorted_counts[-1]
    return most - least


if __name__ == '__main__':
    with open('input') as f:
        template, rules = parse_input(f.read())
    main()
