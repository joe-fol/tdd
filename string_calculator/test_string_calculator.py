import unittest

from string_calculator import add


class TestAdd(unittest.TestCase):
    def test_empty_string_returns_0(self):
        assert add("") == "0"

    def test_given_1_returns_1(self):
        assert add("1") == "1"

    def test_given_3_returns_3(self):
        assert add("3") == "3"

    def test_can_add_two_numbers(self):
        assert add("1,1") == "2"


if __name__ == "__main__":
    unittest.main()
