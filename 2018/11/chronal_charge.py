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


def largest_3x3_power(grid, width=300, height=300):
    """Find the 3x3 square with the largest power and return it's x,y
       coordinates."""
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

    return coord_of_largest


def largest_power_square(grid, starting_sq_size=3):
    """Find the (size x size)-grid with the largest power in the grid and
    return the x,y coordinate of the top-left fuel cell of that square."""
    # Brute force
    largest_power = 0
    coord_of_largest = (None, None, None)  # (x, y, sq_size)

    for sq_size in range(1, len(grid)):
        print("sq_size: " + str(sq_size), end=" ")
        for x in range(0, len(grid) - sq_size):
            for y in range(0, len(grid) - sq_size):
                sq_power = sum(grid[x_][y_]
                               for x_ in range(x, x+sq_size)
                               for y_ in range(y, y + sq_size))
                if sq_power > largest_power:
                    largest_power = sq_power
                    coord_of_largest = (x, y, sq_size)
        print(coord_of_largest)

    return coord_of_largest


grid = create_grid()

# part one
print(largest_3x3_power(grid))

# part two
print(largest_power_square(grid, 1))
