__author__ = "Ky Kartchner"
__date__ = "6/12/20"

from main import base_conversion
import unittest


class TestMain(unittest.TestCase):
    def test_valid_values(self):
        self.assertEqual(base_conversion(23, 2), "10111",
                         "23 in base 2 should be 10111")
        self.assertEqual(base_conversion(23, 8), "27",
                         "23 in base 8 should be 27")
        self.assertEqual(base_conversion(23, 16), "17",
                         "23 in base 16 should be 17")
        self.assertEqual(base_conversion(138, 2), "10001010",
                         "138 in base 2 should be 10001010")
        self.assertEqual(base_conversion(138, 8), "212",
                         "138 in base 8 should be 212")
        self.assertEqual(base_conversion(138, 16), "8A",
                         "138 in base 16 should be 8A")

    def test_negative_number(self):
        self.assertRaises(ValueError, base_conversion, -32, 2)


if __name__ == "__main__":
    unittest.main()
