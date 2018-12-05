def triplet_or_pair(id):
    """Checks if an id has a triplet and/or a pair. Returns a tuple containing
    two booleans."""
    values = set(id)

    similar_values_count = []
    for x in values:
        similar_values_count.append(id.count(x))

    has_triplet = False
    has_pair = False
    if 2 in similar_values_count:
        has_pair = True
    if 3 in similar_values_count:
        has_triplet = True

    return (has_triplet, has_pair)


def part_one():
    with open("ids.txt") as file:
        triplets = 0
        pairs = 0
        for line in file:
            tuple = triplet_or_pair("".join(line))
            if tuple[0]:
                triplets += 1
            if tuple[1]:
                pairs += 1

        # Checksum
        return triplets * pairs

        file.close()


print("Part one answer: " + str(part_one()))
