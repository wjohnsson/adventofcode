input_lines = open("input").read().splitlines()

start_time = int(input_lines[0])
buses = [(i, int(bus)) for i, bus in enumerate(input_lines[1].split(",")) if bus != "x"]

# Part 1
time = start_time - 1
bus = None
found = False

while not found:
    time += 1
    for _, b in buses:
        if time % b == 0:
            bus = b
            found = True

print(f"Part 1: {bus * (time - start_time)}")  # 115

# Part 2
# All departure times look suspiciously prime??? edit: they are, probably for a reason
time = step = 1
for i, bus in buses:
    # Step until we find the first time that works for this bus and preceding buses
    while (time + i) % bus != 0:
        time += step
    # Because all buses are prime we can increase the step size
    step *= bus

print(f"Part 2: {time}")  # 756261495958122
