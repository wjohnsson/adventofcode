import re
from collections import defaultdict

raw = open("input").read()
parts = raw.split("\n\n")

def get_rules(numbers):
    rules_input = parts[0].splitlines()
    rules = defaultdict(list)
    for line in rules_input:
        a, b = map(int, line.split("|"))
        if a in numbers and b in numbers:
            rules[a].append(b)
    return rules

def is_ok(update, rules):
    seen = set()
    for current in update:
        rule = rules[current]
        for number_must_be_after in rule:
            if number_must_be_after in seen:
                return False
        seen.add(current)
    return True

def middle(ll):
    return ll[len(ll) // 2]

# Part 2
def get_ordering(update):
    numbers_to_check = update[:]
    R = get_rules(update)
    ordering = dict()
    order_scalar = 0

    while numbers_to_check:
        for number in numbers_to_check:
            if number not in R.keys() or R[number] == []:
                ordering[number] = order_scalar
                order_scalar -= 1

                R.pop(number, None)
                for _, item in R.items():
                    item.remove(number)
                numbers_to_check.remove(number)
                break
    return ordering

all_numbers = set(int(n) for n in re.findall(r"\d+", raw))
rules = get_rules(all_numbers)
updates = [list(map(int, digits)) for digits in map(lambda line: re.findall(r"\d+", line), parts[1].splitlines())]
print("Part 1:", sum(middle(update) for update in updates if is_ok(update, rules)))

bad_updates = [update for update in updates if not is_ok(update, rules)]
total = 0
for update in bad_updates:
    ordering = get_ordering(update)
    total += middle(sorted(update, key=(lambda x: ordering[x])))

print("Part 2:", total)

