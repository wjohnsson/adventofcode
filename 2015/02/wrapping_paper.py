input_lines = open("input").read().splitlines()

dimensions = [list(map(int, x.split("x"))) for x in input_lines]

total_paper = 0
total_ribbon = 0
for l, w, h in dimensions:
    # Part 1
    slack = min(l*w, w*h, h*l)
    total_paper += 2*l*w + 2*w*h + 2*h*l + slack

    # Part 2
    wrap = 2 * min(l+w, l+h, w+h)
    ribbon = l*w*h
    total_ribbon += wrap + ribbon


print("Part 1", total_paper)  # 1598415
print("Part 2", total_ribbon)  # 3812909
