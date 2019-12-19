# space_image_format.py
# solution to https://adventofcode.com/2019/day/8


def parse_input(inp, layer_width, layer_height):
    digits = list(reversed(inp))
    layers = []
    while len(digits) > 0:
        rows = []
        for _ in range(layer_height):
            row = []
            for _ in range(layer_width):
                row.append(digits.pop())
            rows.append(row)
        layers.append(rows)
    return layers


def fewest_zeroes(layers):
    fewest = float("inf")
    layer_with_fewest = layers[0]
    for layer in layers:
        zeroes = sum([row.count(0) for row in layer])

        if zeroes < fewest:
            fewest = zeroes
            layer_with_fewest = layer
    return layer_with_fewest


def checksum(layer):
    """
    Return the number of 1 digits multiplied by the number of 2 digits.
    """
    ones = sum([row.count(1) for row in layer])
    twos = sum([row.count(2) for row in layer])
    return ones * twos


def pixel_color(x, y, layers):
    """
    Return the color of the topmost non-transparent layer.
    """
    for layer in layers:
        color = layer[y][x]
        if color != 2:
            return color


def decode_image(layers):
    width = len(layers[0][0])
    height = len(layers[0])
    image = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixel_color(x, y, layers))
        image.append(row)
    return image


def print_image(image):
    for y in range(len(image)):
        for x in range(len(image[y])):
            color = image[y][x]
            if color == 0:
                print("█", end="")
            elif color == 1:
                print("░", end="")
        print()


password = [int(n) for n in open("input.txt").readline()]

# Part 1
print(checksum(fewest_zeroes(parse_input(password, 25, 6))))  # 2375

# Part 2
print_image(decode_image(parse_input(password, 25, 6)))  # RKHRY
