import pytest
from calc import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


@pytest.mark.parametrize("a, b, expected", [
    (-1, -4, -5),
    (5, -3, 2),
    (-7, 4, -3),
])
def test_add_negative_numbers(a, b, expected):
    assert add(a, b) == expected


def test_add_zero():
    assert add(0, 7) == 7
    assert add(12, 0) == 12


def test_add_floats():
    assert add(1.2, 3.6) == pytest.approx(4.8)


def test_add_large_numbers():
    assert add(10**12, 12**14) == 10**12 + 12**14


def test_add_type_error_string():
    with pytest.raises(TypeError):
        add("2", 5)


def test_add_type_error_none():
    with pytest.raises(TypeError):
        add(None, 9)


def test_add_type_error_list():
    with pytest.raises(TypeError):
        add([1, 2, 3], 6)
