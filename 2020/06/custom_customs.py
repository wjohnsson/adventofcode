from collections import defaultdict

groups = open("input").read().split("\n\n")

# Part 1
combined_answers = [group.replace("\n", "") for group in groups]
print(f"Part 1: {sum([len(set(answers)) for answers in combined_answers])}")  # 6596

# Part 2
split_answers = [group.split("\n") for group in groups]
total_count = 0
for group in split_answers:  # the group's answers
    yeses = defaultdict(int)
    for dudes_answers in group:  # one dude belonging to the group
        for yes in dudes_answers:
            yeses[yes] += 1

    # It only counts if everyone said yes.
    total_count += sum([yes_count == len(group) for yes_count in yeses.values()])

print(f"Part 2: {total_count}")  # 3219
