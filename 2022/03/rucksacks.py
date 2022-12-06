backpacks = open('input').read().split()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_prio = dict((letter, alphabet.rfind(letter) + 1) for letter in alphabet)

# Part 1
prio_sum = 0
for backpack in backpacks:
    mid = len(backpack) // 2
    first_half = set(backpack[:mid])
    second_half = set(backpack[mid:])

    common_letter = (first_half & second_half).pop()
    prio_sum += letter_prio[common_letter]

print(prio_sum)

# Part 2
groups = [map(set, backpacks[i:i+3]) for i in range(0, len(backpacks), 3)]

prio_sum = 0
for group in groups:
    common_letter = set.intersection(*group).pop()
    prio_sum += letter_prio[common_letter]

print(prio_sum)
