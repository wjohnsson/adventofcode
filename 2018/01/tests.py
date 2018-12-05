import unittest
import chronal_calibration as cc
import os


# For learning how to make unit tests in python.
class TestChronalCalibration(unittest.TestCase):

    @staticmethod
    def write_numbers_to_file(file, numbers):
        """Helper function"""
        for num in numbers:
            if num > 0:
                file.write("+" + str(num) + "\n")
            else:
                file.write(str(num) + "\n")
            file.flush()

    def test_part_one(self):
        test_file = open("tests.txt", "w+")

        list1 = [1, -2, 3, 1]
        list2 = [1, 1, 1]
        list3 = [1, 1, -2]
        list4 = [-1, -2, -3]

        self.write_numbers_to_file(test_file, list1)
        self.assertEqual(cc.part_one("tests.txt"), 3)
        test_file.seek(0)
        test_file.truncate()

        self.write_numbers_to_file(test_file, list2)
        self.assertEqual(cc.part_one("tests.txt"), 3)
        test_file.seek(0)
        test_file.truncate()

        self.write_numbers_to_file(test_file, list3)
        self.assertEqual(cc.part_one("tests.txt"), 0)
        test_file.seek(0)
        test_file.truncate()

        self.write_numbers_to_file(test_file, list4)
        self.assertEqual(cc.part_one("tests.txt"), -6)

        test_file.close()
        os.remove("tests.txt")
