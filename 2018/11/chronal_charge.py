# puzzle input
SERIAL_NUMBER = 2694

class FuelCell:

    def __init__(self, x, y, serial_number):
        self.x = x
        self.y = y
        self.serial_number = serial_number
        self.power_level()

    def power_level(self):
        """Calculate the power level of a fuel cell."""
        rack_id = self.x + 10
        self.power_level = rack_id * self.y
        self.power_level += self.serial_number
        self.power_level *= rack_id
        self.power_level = (self.power_level // 100) % 10
        self.power_level -= 5

    def __str__(self):
        return str(self.x) + "," + str(self.y) + ", serial number " + str(self.serial_number) + ": power level " + str(self.power_level) + "."


def largest_power_square():
    """Returns the X,Y coordinate of the top-left fuel cell of the 3x3 square
       of the largest power."""
    fc = FuelCell(0, 0, SERIAL_NUMBER)
    return fc

# Testing
print(FuelCell(122, 79, 57))
print(FuelCell(217, 196, 39))
print(FuelCell(101, 153, 71))
