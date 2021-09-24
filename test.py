import pytest
import math


class TestFloat:
    @pytest.mark.parametrize(
        "test_input,expected", [("0.012", 0.012), (7, 7.0), ("inf", math.inf)]
    )
    def test_casting(self, test_input, expected):
        assert float(test_input) == expected

    def test_ratio(self):
        a = 1.0
        x, y = a.as_integer_ratio()
        assert x == y
        b = 1.76
        z, e = b.as_integer_ratio()
        assert z > e

    def test_integer(self):
        a = 5.5
        assert not a.is_integer()
        b = 5.0
        assert b.is_integer()


class TestTuple:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ([1, 2], (1, 2)),
            ({1: "a", 2: "b"}, (1, 2)),
            ("12", ("1", "2")),
            ("", tuple()),
        ],
    )
    def test_casting(self, test_input, expected):
        assert tuple(test_input) == expected

    def test_assign(self):
        a = (1, 2, 3)
        try:
            a[3] = 4
        except TypeError:
            pass

    def test_index_count(self):
        a = (1, 2, 2, 2)
        assert a.index(2) == 1
        assert a.count(2) == 3
