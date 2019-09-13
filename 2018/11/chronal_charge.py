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


def largest_power_square(grid, starting_grid_size=3):
    """Find the (size x size)-grid with the largest power in the grid and
    return the x,y coordinate of the top-left fuel cell of that square."""
    # Brute force
    largest_total = 0
    coord_of_largest = [0, 0, 0]  # [x, y, grid_size]

    for grid_size in range(starting_grid_size, 301):
        for x in range(0, 301 - grid_size):
            for y in range(0, 301 - grid_size):
                # Find total power of (size x size) square
                total_power = 0
                for i in range(0, grid_size):
                    for j in range(0, grid_size):
                        total_power += grid[x + i][y + j]

                        if total_power > largest_total:
                            # New largest total power found
                            largest_total = total_power
                            coord_of_largest[0] = x
                            coord_of_largest[1] = y
                            coord_of_largest[2] = grid_size

        # For debugging
        print("Testing grid size: " + str(grid_size) +
              ". Current largest total power found: " +
              str(largest_total) + ". at " +
              str(coord_of_largest[:2]) +
              " with grid size " +
              str(coord_of_largest[2]))

    return coord_of_largest


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


grid = create_grid()

# part one
print(largest_3x3_power(grid))

# part two test
test_grid1 = create_grid(serial_number=18)
test_grid2 = create_grid(serial_number=42)
print(largest_power_square(test_grid1, starting_grid_size=16))
print(largest_power_square(test_grid2))

print(largest_power_square(grid))
print(largest_power_square(grid))
