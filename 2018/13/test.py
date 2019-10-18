import cart
import copy
import unittest


class TestMinecartMadness(unittest.TestCase):
    def test_rotations(self):
        """
        Tests if carts are able to rotate as described
        in the problem description
        """
        cart1 = cart.Cart(0, 0, "^")
        cart1.left()
        self.assertEqual(cart1.dir, "<",
                         "Turning the cart: (" + str(cart1) + ") left should make it face left")
        cart1.right()
        self.assertEqual(cart1.dir, "^",
                         "Turning the cart: (" + str(cart1) + ") right should make it face up")
        cart1.right()
        self.assertEqual(cart1.dir, ">",
                         "Turning the cart: (" + str(cart1) + ") right should make it face right")
        cart1.right()
        self.assertEqual(cart1.dir, "v",
                         "Turning the cart: (" + str(cart1) + ") right should make it face down")
        cart1.left()
        self.assertEqual(cart1.dir, ">",
                         "Turning the cart: (" + str(cart1) + ") right should make it face right")

        # Test intersection behavior
        cart2 = copy.deepcopy(cart1)
        cart1.turn()
        cart2.left()
        self.assertEqual(cart1.dir, cart2.dir,
                         "Cart should turn left the first time it reaches an intersection")

        cart1.turn()
        self.assertEqual(cart1.dir, cart2.dir,
                         "Cart should not turn at all the second time it reaches an intersection")

        cart1.turn()
        cart2.right()
        self.assertEqual(cart1.dir, cart2.dir,
                         "Cart should turn right the third time it reaches an intersection")
