from square import Square
from triangle import Triangle
import pytest


def test_init_square():
    s = Square(12)
    assert True


def test_area_square():
    s = Square(4)
    assert s.area == 4 * 4


def test_change_area_square():
    s = Square(4)
    f_area = s.area
    s.a = 5
    assert s.area != f_area and s.area == 5 * 5


def test_perimeter_square():
    s = Square(3)
    assert s.perimeter == 3 * 4


def test_change_perimeter_square():
    s = Square(3)
    f_perimeter = s.perimeter
    s.a = 4
    assert s.perimeter != f_perimeter and s.perimeter == 4 * 4


def test_add_area_square():
    s = Square(4)
    f_area = s.area
    t = Triangle(12, 13, 14)
    s.add_area(t)
    assert s.area == f_area + t.area


def test_neg_add_area_square():
    s = Square(4)
    with pytest.raises(ValueError):
        s.add_area(13)
