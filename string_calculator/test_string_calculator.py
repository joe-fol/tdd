import unittest

from string_calculator import add


class TestAdd(unittest.TestCase):
    def test_empty_string_returns_0(self):
        self.assertEqual(add(""), 0)


if __name__ == "__main__":
    unittest.main()
