import unittest
from day05 import *


class TestConditions(unittest.TestCase):

    def test_vowels(self):
        self.assertTrue(at_least_three_vowels("aei"))
        self.assertTrue(at_least_three_vowels("aaa"))
        self.assertTrue(at_least_three_vowels("xazegov"))
        self.assertFalse(at_least_three_vowels("a"))

    def test_one_letter_twice(self):
        self.assertTrue(one_letter_twice("abcdde"))
        self.assertTrue(one_letter_twice("aabbccdd"))
        self.assertFalse(one_letter_twice("abcd"))

    def test_twice_no_overlap(self):
        self.assertTrue(twice_no_overlap("xyxy"))
        self.assertTrue(twice_no_overlap("aabcdefgaa"))
        self.assertFalse(twice_no_overlap("aaa"))

        self.assertTrue(twice_no_overlap("qjhvhtzxzqqjkmpb"))
        self.assertTrue(twice_no_overlap("xxyxx"))
        self.assertTrue(twice_no_overlap("uurcxstgmygtbstg"))
        self.assertFalse(twice_no_overlap("ieodomkazucvgmuy"))

    def test_repeats_with_pad(self):
        self.assertTrue(repeats_with_pad("xyx"))
        self.assertTrue(repeats_with_pad("abcdefeghi"))  # efe
        self.assertTrue(repeats_with_pad("aaa"))

        self.assertTrue(repeats_with_pad("qjhvhtzxzqqjkmpb"))  # zxz
        self.assertTrue(repeats_with_pad("xxyxx"))  # xyx
        self.assertFalse(repeats_with_pad("uurcxstgmygtbstg"))
        self.assertTrue(repeats_with_pad("ieodomkazucvgmuy"))  # odo

