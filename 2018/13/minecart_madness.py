# minecart_madness.py
# solution to https://adventofcode.com/2018/day/13

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
    """Turns a cart if it is standing on a curve or intersection"""
    try:
        # If the tracks aren't fully connected, a cart might derail
        track = tracks[cart.y][cart.x]
    except IndexError:
        print("Cart " + str(cart) + " derailed!")
        raise

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


def print_state(tracks, carts):
    """
    Print tracks and location of carts for visualizing or debugging smaller
    maps
    """
    cart_dict = dict()
    for cart in carts:
        cart_dict[(cart.x, cart.y)] = cart

    for y in range(len(tracks)):
        for x, track in enumerate(tracks[y]):
            try:
                cart = cart_dict[(x, y)]
                print(cart.dir, end="")
            except KeyError:
                print(track, end="")
        print()  # newline


def collision(carts):
    positions = set()
    set_length = 0
    for cart in carts:
        set_length = len(positions)
        positions.add((cart.x, cart.y))
        if len(positions) == set_length:
            # If we add something to the set, but the length didn't change, we
            # know there's a collision
            return True
    return False


def first_crash(input_file_lines):
    """Returns solution to part one, the location of the first crash"""
    tracks, carts = create_map(input_file_lines)

    while True:
        list.sort(carts)  # let top most cart move first

        for cart in carts:
            cart.move()

            if collision(carts):
                return (cart.x, cart.y)

            turn_cart(tracks, cart)


def answer_part_one():
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, "input_track")
    print("First crash at " +
          str(first_crash(open(file_path).readlines())))
