from cart import Cart
import unittest


class TestMinecartMadness(unittest.TestCase):
    def test_cart_left_right_rotations(self):
        """
        Tests if rotating carts left and right works as intended
        """
        cart1 = Cart(0, 0, "^")
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

    def test_cart_intersection_behavior(self):
        """
        Tests if carts are able to rotate in the correct order when reaching
        intersections
        """
        #
        # v        This case tests if
        # |        a cart would follow
        # +--+--+  the lines as shown
        #       |  in the figure
        #       +--+----
        cart1 = Cart(0, 0, "v")
        cart1.turn()
        self.assertEqual(cart1.dir, ">",
                         "Cart should turn left the first time it reaches an intersection")

        prev_dir = cart1.dir
        cart1.turn()
        self.assertEqual(cart1.dir, prev_dir,
                         "Cart should not turn at all the second time it reaches an intersection")

        cart1.turn()
        self.assertEqual(cart1.dir, "v",
                         "Cart should turn right the third time it reaches an intersection")
        cart1.turn()
        self.assertEqual(cart1.dir, ">",
                         "Cart should turn left the fourth time it reaches an intersection")
        cart1.turn()
        self.assertEqual(cart1.dir, ">",
                         "Cart should not turn at all the fifth time it reaches an intersection")
        # etc...

        #    +---
        #    |     This case tests if
        #    +     a cart would follow
        #    |     the lines as shown
        # >--+     in the figure
        #
        cart2 = Cart(0, 0, ">")
        cart2.turn()
        self.assertEqual(cart2.dir, "^",
                         "Cart should turn left the first time it reaches an intersection")

        prev_dir = cart2.dir
        cart2.turn()
        self.assertEqual(cart2.dir, prev_dir,
                         "Cart should not turn at all the second time it reaches an intersection")

        cart2.turn()
        self.assertEqual(cart2.dir, ">",
                         "Cart should turn right the third time it reaches an intersection")
