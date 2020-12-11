boarding_passes = [str.strip(line) for line in open("input").readlines()]


def binary_partition(lo, hi, cs, lower_char, upper_char):
    for c in cs:
        mid = lo + ((hi - lo) // 2)
        if c == lower_char:
            hi = mid
        elif c == upper_char:
            lo = mid + 1
    return lo


seat_ids = []
for bp in boarding_passes:
    bp_row, bp_col = bp[:7], bp[-3:]
    row = binary_partition(0, 127, bp_row, "F", "B")
    col = binary_partition(0, 7, bp_col, "L", "R")
    seat_ids.append(row * 8 + col)

# Part 1
seat_ids = sorted(seat_ids)
hsi = seat_ids[-1]  # highest seat ID
print(f"Part 1: {hsi}")  # 978

# Part 2
lsi = seat_ids[0]  # lowest seat ID

# s = what the sum would be if all seats in the range [lsi, hsi] was in the list.
s = (hsi - lsi + 1) * ((hsi + lsi) / 2)

# The missing seat is then the difference from the actual sum.
missing_seat_id = s - sum(seat_ids)
print(f"Part2: {int(missing_seat_id)}")  # 727
