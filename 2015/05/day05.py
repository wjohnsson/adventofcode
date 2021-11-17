def main():
    input_lines = open("input").read().splitlines()
    nice_part1, nice_part2 = 0, 0
    for s in input_lines:
        # Part 1
        if at_least_three_vowels(s) and \
           one_letter_twice(s) and \
           not has_disallowed_substrings(s):
            nice_part1 += 1
        # Part 2
        if twice_no_overlap(s) and repeats_with_pad(s):
            nice_part2 += 1

    print("Part 1:", nice_part1)  # 258
    print("Part 2:", nice_part2)  # 53


def at_least_three_vowels(s):
    total_vowels = 0
    for vowel in "aeiou":
        total_vowels += s.count(vowel)
    return total_vowels >= 3


def one_letter_twice(s):
    # Dunno what happens if the string is an odd length
    assert len(s) % 2 == 0
    for c1, c2 in zip(s, s[1:]):
        if c1 == c2:
            return True
    return False


def has_disallowed_substrings(s):
    for substring in ["ab", "cd", "pq", "xy"]:
        if substring in s:
            return True
    return False


def twice_no_overlap(s):
    pairs = list(zip(s, s[1:]))
    indexed_pairs = list(enumerate(pairs))

    appears_twice = []
    for pair in set(pairs):
        count = pairs.count(pair)
        if count > 2:
            # Special case if there's more than two of one pair,
            # two of them must be non-overlapping
            return True
        elif count == 2:
            # Otherwise we need to check for overlaps
            appears_twice.append(pair)

    if len(appears_twice) == 0:
        return False

    # Keep pairs of characters that appear twice
    filtered_pairs = [(i, a + b) for (i, (a, b)) in indexed_pairs if (a, b) in appears_twice]

    # Check for overlap between pairs
    overlaps = 0
    for (index1, pair1), (index2, pair2) in zip(filtered_pairs, filtered_pairs[1:]):
        if index1 == index2 - 1 and pair1 == pair2:
            overlaps += 1

    # We know that there are only pairs that appear twice (would've already returned otherwise)
    # so if at least one of them doesn't overlap we return True
    candidates = len(filtered_pairs) // 2
    return overlaps != candidates


def repeats_with_pad(s):
    for i in range(len(s) - 2):
        c1, _, c2 = s[i:i + 3]
        if c1 == c2:
            return True
    return False


if __name__ == "__main__":
    main()
