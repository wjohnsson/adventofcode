import re

lines = open('input').read().split()

pattern = re.compile(r'\d+')
pairs = [list(map(int, pattern.findall(line))) for line in lines]

# Part 1
print(sum(1 for a, b, c, d in pairs if (a <= c and b >= d) or (c <= a and d >= b)))

# Part 2
print(sum(1 for a, b, c, d in pairs if
          c <= a <= d or
          c <= b <= d or
          a <= c <= b or
          a <= d <= b))
