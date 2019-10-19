from cart import Cart
import minecart_madness
import unittest
import os


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

    def test_vertical_straight_track(self):
        """
        Tests a simple vertical track to see where the first crash occurs
        """
        # Vertical straight track
        #   0          0           0
        # 0 |          |           |
        # 1 v          |           |
        # 2 |          v           |
        # 3 |  tick -> |  tick ->  X
        # 4 |          ^           |
        # 5 ^          |           |
        # 6 |          |           |
        #
        # should return (0,3)

        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, "test_straight_vertical_track")
        with open(file_path) as f:
            test_lines = f.readlines()
            tick, pos = minecart_madness.first_crash(test_lines)
            self.assertEqual(pos, (0, 2),
                             "Moving topmost cart first every tick should" +
                             " result in a crash at (0,3)")


if __name__ == '__main__':
    unittest.main()
