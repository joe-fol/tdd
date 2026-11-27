import pytest

from string_calculator import add


class TestAdd:
    def test_empty_string_returns_0(self):
        assert add("") == "0"

    @pytest.mark.parametrize(
        "numbers,expected",
        [
            ("1", "1"),
            ("2", "2"),
            ("1,1", "2"),
            ("2,3", "5"),
            ("1.1, 1.4", "2.5"),
            ("1.1, 1.2", "2.3"),
            ("1,2,3,4,5", "15"),
            ("1,2.37,3,4.29,5", "15.66"),
        ],
    )
    def test_can_add_numbers_from_string(self, numbers, expected):
        assert add(numbers) == expected
