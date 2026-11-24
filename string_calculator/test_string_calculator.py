import pytest

from string_calculator import add


class TestAdd:
    def test_empty_string_returns_0(self):
        assert add("") == "0"

    def test_given_1_returns_1(self):
        assert add("1") == "1"

    def test_given_3_returns_3(self):
        assert add("3") == "3"

    @pytest.mark.parametrize(
        "numbers,expected",
        [
            ("1,1", "2"),
            # Todo Joe to make this pass...
            ("2,3", "5"),
        ]
    )
    def test_can_add_two_numbers(self, numbers, expected):
        assert add(numbers) == expected
