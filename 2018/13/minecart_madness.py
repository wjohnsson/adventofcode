import os
import copy
from cart import Cart
from cart import cart_symbols

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, "test_small_track")

tracks = [x.rstrip() for x in open(file_path).readlines()]
carts = []

for y in range(len(tracks)):
    for x in range(len(tracks[y])):
        symbol = tracks[y][x]
        if symbol in cart_symbols:
            carts.append(Cart(x, y, symbol))

            # Place a track piece underneath this cart
            if symbol in "v^":
                tracks[y] = tracks[y].replace(symbol, "|", 1)
            if symbol in "<>":
                tracks[y] = tracks[y].replace(symbol, "-", 1)


def turn_cart():
    """Turns a cart if it is now standing on a curve or intersection"""
    track = tracks[cart.y][cart.x]

    if track == "\\":
        if cart.dir in "^v":
            cart.left()   # ⮡ ⮢
        elif cart.dir in "<>":
            cart.right()  # ⮧ ⮤
    elif track == "/":
        if cart.dir in "^v":
            cart.right()  # ⮣ ⮠
        elif cart.dir in "<>":
            cart.left()   # ⮥ ⮦
    elif track == "+":
        cart.turn()


def test_rotations():
    """A cart named jimmy going through some tests"""
    jimmy = Cart(0, 0, "^")
    jimmy.left()
    assert jimmy.dir == "<"
    jimmy.right()
    assert jimmy.dir == "^"
    jimmy.right()
    assert jimmy.dir == ">"
    jimmy.right()
    assert jimmy.dir == "v"

    sophie = copy.deepcopy(jimmy)
    jimmy.turn()  # should turn left
    sophie.left()
    assert jimmy.dir == sophie.dir
    jimmy.turn()  # should not turn
    assert jimmy.dir == sophie.dir
    jimmy.turn()  # should turn right
    sophie.right()
    assert jimmy.dir == sophie.dir


test_rotations()

tick = 0
while True:
    list.sort(carts)  # top most cart moves first
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

        turn_cart()

    tick += 1
