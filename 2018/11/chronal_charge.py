# puzzle input
SERIAL_NUMBER = 2694


def power_level(x, y, serial_number):
    """Calculate the power level of a fuel cell with the given coordinates."""
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    return power_level - 5


def largest_power_square_coord(width, height, serial_number):
    """Returns the X,Y coordinate of the top-left fuel cell of the 3x3 square
       with the largest power."""
    grid = []
    for x in range(0, width + 1):
        row = []
        for y in range(0, height + 1):
            row.append(power_level(x, y, serial_number))
        grid.append(row)

    # Brute force
    largest_total = 0
    coord_of_largest = [0, 0]  # [x, y]

    for x in range(0, width - 2):
        for y in range(0, height - 2):
            # Find total power of 3x3 square
            total_power = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    total_power += grid[x + i][y + j]

            if total_power > largest_total:
                # New largest total power found
                largest_total = total_power
                coord_of_largest[0] = x
                coord_of_largest[1] = y

    print(str(largest_total))
    return coord_of_largest


# Tests
print(largest_power_square_coord(300, 300, 18))
print(largest_power_square_coord(300, 300, 42))

# part one
print(largest_power_square_coord(300, 300, SERIAL_NUMBER))
