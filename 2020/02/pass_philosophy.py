policies = open("input").readlines()
valid_p1 = valid_p2 = 0

for policy in policies:
    # r represents a range in part 1 and positions in part 2.
    r = list(map(int, policy.split(" ")[0].split("-")))
    c = policy.split(":")[0][-1]  # password character
    p = policy.split(" ")[-1]  # password

    # Part 1
    if p.count(c) in range(r[0], r[1] + 1):
        valid_p1 += 1

    # Part 2
    # check the condition using xor (requires explicit cast to bool)
    if bool(p[r[0] - 1] == c) ^ bool(p[r[1] - 1] == c):
        valid_p2 += 1

print(f"Part 1: {valid_p1}")  # 655
print(f"Part 2: {valid_p2}")  # 673
