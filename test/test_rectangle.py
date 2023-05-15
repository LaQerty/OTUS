from rectangle import Rectangle
from square import Square
import pytest


def test_init_rectangle():
    try:
        r = Rectangle(12, 12)
    except:
        assert False
    assert True


def test_area_rectangle():
    r = Rectangle(4, 5)
    assert r.area == 4 * 5


def test_change_area_rectangle():
    r = Rectangle(4, 5)
    f_area = r.area
    r.a = 5
    assert r.area != f_area and r.area == 5 * 5


def test_perimeter_rectangle():
    r = Rectangle(4, 5)
    assert r.perimeter == 2 * 4 + 2 * 5


def test_change_perimeter_rectangle():
    r = Rectangle(4, 5)
    f_perimeter = r.perimeter
    r.a = 5
    assert r.perimeter != f_perimeter and r.perimeter == 2 * 5 + 2 * 5


def test_add_area_rectangle():
    r = Rectangle(4, 4)
    f_area = r.area
    s = Square(12)
    try:
        r.add_area(s)
    except ValueError:
        assert False
    assert r.area == f_area + s.area


def test_neg_add_area_rectangle():
    r = Rectangle(4, 4)
    try:
        r.add_area(13)
        assert False
    except ValueError:
        assert True
