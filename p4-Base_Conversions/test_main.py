__author__ = "Ky Kartchner"

from main import base_conversion
import unittest


class TestMain(unittest.TestCase):
    def test_valid_values(self):
        self.assertEqual(base_conversion(23, 2), "10111",
                         "23 in base 2 should be '10111'")
        self.assertEqual(base_conversion(23, 16), "17",
                         "23 in base 16 should be '17'")


if __name__ == "__main__":
    unittest.main()
