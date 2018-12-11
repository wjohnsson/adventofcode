class Claim:

    def __init__(self, claim_id, x, y, size_x, size_y):
        self.claim_id = claim_id
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def __str__(self):
        return str(self.x) + "," + str(self.y) + \
               ": " + str(self.size_x) + "x" + str(self.size_y)

def parse_claim(claim):
    """Handles parsing of an input string."""
    # Coordinates on one side, dimensions on the other.
    claim = claim.split(":")

    # Engage splitting fiesta.
    id_and_coords = claim[0].split(",")
    claim_id = id_and_coords[0].split(" ")[0].split("#")[-1]
    x = id_and_coords[0].split(" ")[-1]
    y = id_and_coords[1]

    sizes = claim[1].split("x")
    size_x = sizes[0].lstrip()
    size_y = sizes[-1]

    return Claim(int(claim_id), int(x), int(y), int(size_x), int(size_y))


def empty_fabric():
    """Creates an empty fabric where each element is a square inch."""
    return [[0 for _ in range(1000)] for _ in range(1000)]


def part_one():
    with open("claims.txt") as f:
        fabric = empty_fabric()
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


def empty_id_fabric():
    """Creates an empty fabric where each element is a tuple containing the claim_id of the top layer and amount
    of layers below it."""
    return [[[0, 0] for _ in range(1000)] for _ in range(1000)]


def part_two():
    with open("claims.txt") as f:
        fabric = empty_id_fabric()
        claims = [parse_claim(c) for c in f.readlines()]

        for claim in claims:
            for x in range(claim.size_x):
                for y in range(claim.size_y):
                    # Add a layer to the specified square inch of fabric and update
                    # the top layer.
                    fabric[x + claim.x][y + claim.y][0] = claim.claim_id
                    fabric[x + claim.x][y + claim.y][1] += 1

        # Find the claim of fabric with no overlap
        no_overlap_claim = None
        for row in range(len(fabric)):
            for col in range(len(fabric[row])):
                if fabric[row][col][1] == 1:
                    claim_id = fabric[row][col][0]

        return claim_id
        f.close()


print("Answer part one: " + str(part_one()))
print("Answer part two: " + str(part_two()))
