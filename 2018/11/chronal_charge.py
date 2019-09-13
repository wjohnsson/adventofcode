# puzzle input
SERIAL_NUMBER = 2694


def power_level(x, y, serial_number):
    """Calculate the power level of a fuel cell with the given coordinates and
       return it"""
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    return power_level - 5


def create_grid(serial_number=SERIAL_NUMBER):
    """Calculate power level for all coordinates and return a 2 dimensional
       list representing the grid."""
    grid = []
    for x in range(0, 300 + 1):
        row = []
        for y in range(0, 300 + 1):
            row.append(power_level(x, y, serial_number))
        grid.append(row)
    return grid


def largest_power_square(grid, sq_size):
    """Find the (sq_size x sq_size)-square with the largest power in the grid and
    return the x,y coordinate of the top-left fuel cell of that square."""
    # (x, y, square size, largest power)
    largest = (None, None, None, 0)

    for x in range(0, len(grid) - sq_size):
        for y in range(0, len(grid) - sq_size):
            sq_power = sum(grid[x_][y_]
                           for x_ in range(x, x+sq_size)
                           for y_ in range(y, y + sq_size))
            if sq_power > largest[3]:
                largest = (x, y, sq_size, sq_power)

    return largest


grid = create_grid()

# part one
result = largest_power_square(grid, 3)
print(str(result[0]) + "," + str(result[1]) + "\n\n")

# part two
# Brute force O(n^5)
result = (None, None, None, 0)
for sq_size in range(3, len(grid)):
    print(result)
    temp = largest_power_square(grid, sq_size)
    if result[3] < temp[3]:
        result = temp
