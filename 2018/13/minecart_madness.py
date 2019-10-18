import os
from cart import Cart
from cart import cart_symbols


def create_map(input_file_lines):
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
    tracks = tracks[cart.y][cart.x]

    if tracks == "\\":
        if cart.dir in "^v":
            cart.left()   # ⮡ ⮢
        elif cart.dir in "<>":
            cart.right()  # ⮧ ⮤
    elif tracks == "/":
        if cart.dir in "^v":
            cart.right()  # ⮣ ⮠
        elif cart.dir in "<>":
            cart.left()   # ⮥ ⮦
    elif tracks == "+":
        cart.turn()


def first_crash(input_file_lines):
    """Prints solution to part one, the location of the first crash"""
    carts, tracks = create_map(input_file_lines)

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
                print("####### CART CRASH REPORT ######")
                print("tick: " + str(tick + 1))
                print("crash at: " + str(pos))
                exit()

            turn_cart(tracks, cart)

        tick += 1


# part one
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, "test_small_track")
first_crash(open(file_path).readlines())
