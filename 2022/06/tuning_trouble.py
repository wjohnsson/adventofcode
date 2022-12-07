from collections import Counter

datastream = open('input').read()

# Part 1 and 2
def first_substring_with_distinct_characters(win_size):
    for i in range(0, len(datastream) - win_size):
        window = datastream[i:i+win_size]
        if all([count == 1 for count in Counter(window).values()]):
            return i + win_size


print(first_substring_with_distinct_characters(4))
print(first_substring_with_distinct_characters(14))