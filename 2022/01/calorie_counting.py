lines = open('input').read().split('\n\n')

elves = []
for elf in lines:
    calories = sum(map(int, elf.split('\n')))
    elves.append(calories)

print(max(elves))
print(sum(sorted(elves, reverse=True)[:3]))
    