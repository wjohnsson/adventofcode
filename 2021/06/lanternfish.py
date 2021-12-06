from functools import lru_cache

fish = list(map(int, open("input").read().rstrip().split(",")))


@lru_cache  # memoize!
def spawn_count(timer_init, days_left):
    days_left -= (timer_init + 1)
    if days_left < 0:
        return 1

    count = spawn_count(8, days_left)
    while days_left >= 7:
        days_left -= 7
        count += spawn_count(8, days_left)

    return 1 + count


print("Part 1:", sum(spawn_count(f, 80) for f in fish))  # 352872
print("Part 2:", sum(spawn_count(f, 256) for f in fish))  # 160704361182149
