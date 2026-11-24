import unittest

from string_calculator import add


class TestAdd(unittest.TestCase):
    def test_empty_string_returns_0(self):
        self.assertEqual(add(""), "0")

    def test_given_1_returns_1(self):
        self.assertEqual(add("1"), "1")

    def test_given_3_returns_3(self):
        self.assertEqual(add("3"), "3")


if __name__ == "__main__":
    unittest.main()
