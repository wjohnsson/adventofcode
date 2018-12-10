class Claim:

    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def __str__(self):
        return str(self.x) + "," + str(self.y) + \
               ": " + str(self.size_x) + "x" + str(self.size_y)


def parse_claim(claim):
    """Parses an input string"""
    # Coordinates on one side, dimensions on the other
    claim = claim.split(":")

    coordinates = claim[0].split(",")
    x = coordinates[0].split(" ")[-1]
    y = coordinates[1]

    sizes = claim[1].split("x")
    size_x = sizes[0].lstrip()
    size_y = sizes[-1]

    return Claim(int(x), int(y), int(size_x), int(size_y))


def part_one():
    with open("claims.txt") as file:
        claims = [parse_claim(c) for c in file.readlines()]

        file.close()


part_one()
