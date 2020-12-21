from collections import defaultdict
from math import prod
import re

input_grouped = open("input").read().split("\n\n")

fields = dict()
for field in input_grouped[0].splitlines():
    # All fields have two ranges, s=start e=end
    name, s1, e1, s2, e2 = re.findall(r"(\D+): (\d+)-(\d+) or (\d+)-(\d+)", field)[0]
    fields[name] = (int(s1), int(e1), int(s2), int(e2))

my_ticket = list(map(int, input_grouped[1].splitlines()[1].split(",")))
tickets = [list(map(int, ticket.split(","))) for ticket in input_grouped[2].splitlines()[1:]]

# ----- Part 1 -----
count = 0
valid_tickets = []  # setup for part 2

for ticket in tickets:
    is_valid = True
    for value in ticket:
        if not any(s1 <= value <= e1 or s2 <= value <= e2 for s1, e1, s2, e2 in fields.values()):
            is_valid = False
            count += value
    if is_valid:
        valid_tickets.append(ticket)

print(f"Part 1: {count}")  # 20058

# ----- Part 2 -----
valid_tickets = list(filter(lambda t: t in valid_tickets, tickets))

# Find the possible index for each field
possible_indexes = defaultdict(list)
for i in range(len(valid_tickets[0])):
    # Take i:th item of every valid ticket
    values = [t[i] for t in valid_tickets]

    for name, ranges in fields.items():
        s1, e1, s2, e2 = ranges
        if all(s1 <= value <= e1 or s2 <= value <= e2 for value in values):
            possible_indexes[name].append(i)

index = dict()
single = None

# Find the index which only works for a single field, assign it to that field
# and remove it as an option for all other fields.
for _ in range(len(possible_indexes)):
    for name, indexes in possible_indexes.items():
        if len(indexes) == 1:
            single = indexes[0]
            # It's only possible for this index to be this field
            index[name] = single

    for indexes in possible_indexes.values():
        if len(indexes) > 0:
            indexes.remove(single)

departure_indexes = [i for name, i in index.items() if name.startswith("departure")]
my_ticket = [val for i, val in enumerate(my_ticket) if i in departure_indexes]

print(f"Part 2: {prod(my_ticket)}")  # 366871907221
