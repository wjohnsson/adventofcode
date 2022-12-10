from collections import defaultdict

lines = open('input').read().rstrip().split('\n')

sizes = defaultdict(int)

current_dir = []
for line in lines:
    if line.startswith('$ cd'):
        directory = line.split()[-1]
        
        if directory == '/':
            current_dir.append('/')
        elif directory == '..':
            current_dir.pop()
        else:
            separator = f'{"/" if current_dir[-1] != "/" else ""}'
            current_dir.append(f'{current_dir[-1]}{separator}{directory}')
    if line[0].isnumeric():
        for directory in current_dir:
            sizes[directory] += int(line.split()[0])

print(f"Part 1: {sum(s for s in sizes.values() if s <= 100_000)}")
print(f"Part 2: {min(s for s in sizes.values() if s >= 30_000_000 - (70_000_000 - sizes['/']))}")