__author__ = "Ky Kartchner"
__date__ = "5/23/2020"

from main import hash_sentence
import unittest


class TestMain(unittest.TestCase):
    def test_hash_valid_values(self):
        self.assertEqual(hash_sentence("hello"), 21)
        self.assertEqual(hash_sentence("pooh bear"), 18)
        self.assertEqual(hash_sentence("We the People of the United States\
            in Order to form a more perfect Union"), 27)

    def test_hash_invalid_value(self):
        self.assertRaises(ValueError, hash_sentence, "101 Dalmations")

    def test_hash_additional_values(self):
        self.assertEqual(hash_sentence("This here is a test"), 30)
        self.assertEqual(hash_sentence("Testing"), 1)
        self.assertRaises(ValueError, hash_sentence, "Th1s has numb3rs")
        self.assertRaises(ValueError, hash_sentence,
                          "th1s h@s numb3rs @nd special $ymb0ls#^*%($)@()!*$")


if __name__ == '__main__':
    unittest.main()
