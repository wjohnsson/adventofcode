from functools import lru_cache
numbers = [int(number) for number in open("input").read().split(" ")]

@lru_cache(maxsize=None)  # memoize!
def count_stones(n, step) -> int:
    if step == 0:
        return 1

    if n == 0:
        return count_stones(1, step - 1)

    s = str(n)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return count_stones(int(s[:mid]), step - 1) + count_stones(int(s[mid:]), step - 1)
    
    return count_stones(n * 2024, step - 1)
    

print("Part 1", sum(count_stones(n, 25) for n in numbers))
print("Part 2", sum(count_stones(n, 75) for n in numbers))