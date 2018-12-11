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
    """Handles parsing of an input string."""
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
    with open("claims.txt") as f:
        # Create an empty fabric where each element is a square inch.
        fabric = [[0 for _ in range(1000)] for _ in range(1000)]

        claims = [parse_claim(c) for c in f.readlines()]

        for claim in claims:
            for x in range(claim.size_x):
                for y in range(claim.size_y):
                    # Add a layer to the specified square inch of fabric.
                    fabric[x + claim.x][y + claim.y] += 1

        # Count overlaps
        overlaps = 0
        for row in range(len(fabric)):
            for col in range(len(fabric[row])):
                if fabric[row][col] >= 2:
                    overlaps += 1

        return overlaps
        f.close()


print("Answer part one: " + str(part_one()))
