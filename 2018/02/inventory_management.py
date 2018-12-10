def triplet_or_pair(items):
    """Checks if an item in a list has a triplet and/or a pair.
    Returns a tuple containing two booleans."""
    values = set(items)

    similar_values_count = []
    for x in values:
        similar_values_count.append(items.count(x))

    has_triplet = False
    has_pair = False
    if 2 in similar_values_count:
        has_pair = True
    if 3 in similar_values_count:
        has_triplet = True

    return has_triplet, has_pair


def part_one():
    with open("ids.txt") as file:
        triplets = 0
        pairs = 0
        for line in file:
            has_triplet_or_pair = triplet_or_pair("".join(line))
            if has_triplet_or_pair[0]:
                triplets += 1
            if has_triplet_or_pair[1]:
                pairs += 1

        # Checksum
        file.close()
        return triplets * pairs


def remove_diff(strings):
    """Finds which characters are common between a pair of strings that differ
    by exactly one item, in a list of strings."""
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            similar_string = []
            common_char = None

            # Assumes the lists are of equal lengths.
            for k in range(len(strings[i])):
                if strings[i][k] != strings[j][k]:
                    similar_string.append(strings[i])
                    common_char = strings[i][k]
                # No need to keep going if at least two differences are found.
                if len(similar_string) > 1:
                    break

            if len(similar_string) == 1:
                return similar_string.pop().replace(common_char, "")


def part_two():
    lines = []
    with open("ids.txt") as file:
        for line in file:
            lines.append(line.rstrip())
        file.close()

    return remove_diff(lines)


print("Part one answer: " + str(part_one()))
print("Part two answer: " + str(part_two()))
