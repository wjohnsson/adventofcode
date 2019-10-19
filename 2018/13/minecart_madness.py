import os
from cart import Cart
from cart import cart_symbols


def create_map(input_file_lines):
    """
    Sets up tracks and carts by reading input file in order to start
    simulating
    """
    tracks = [l.rstrip() for l in input_file_lines]
    carts = []
    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            symbol = tracks[y][x]
            if symbol in cart_symbols:
                carts.append(Cart(x, y, symbol))

                # Place a tracks piece underneath this cart
                if symbol in "v^":
                    tracks[y] = tracks[y].replace(symbol, "|", 1)
                if symbol in "<>":
                    tracks[y] = tracks[y].replace(symbol, "-", 1)
    return tracks, carts


def turn_cart(tracks, cart):
    """Turns a cart if it is now standing on a curve or intersection"""
    track = tracks[cart.y][cart.x]

    if track == "\\":
        if cart.dir in "^v":
            cart.left()   # ⮡ ⮢
        elif cart.dir in "<>":
            cart.right()  # ⮧ ⮤

    if track == "/":
        if cart.dir in "^v":
            cart.right()  # ⮣ ⮠
        elif cart.dir in "<>":
            cart.left()   # ⮥ ⮦

    if track == "+":
        cart.turn()


def first_crash(input_file_lines):
    """ Returns solution to part one, the location of the first crash """
    tracks, carts = create_map(input_file_lines)

    tick = 0  # used for debugging
    while True:
        list.sort(carts)  # let top most cart move first
        positions = set()
        for cart in carts:
            cart.move()

            len_before = len(positions)
            pos = (cart.x, cart.y)
            positions.add(pos)
            if len_before == len(positions):
                return tick, pos

            turn_cart(tracks, cart)

        tick += 1


def answer_part_one():
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, "input_track")
    print("Crash at " +
        str(first_crash(open(file_path).readlines())))
