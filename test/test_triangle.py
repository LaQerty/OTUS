from triangle import Triangle
from circle import Circle
import math
import pytest


def test_init_triangle():
    try:
        t = Triangle(12, 13, 14)
    except:
        assert False
    assert True


def test_uncorrect_values_init_triangle():
    try:
        t = Triangle(1, 3, 14)
        assert False
    except ValueError:
        assert True


def test_area_triangle():
    t = Triangle(4, 5, 6)
    p = t.perimeter / 2
    assert t.area == math.sqrt(p * (p - 4) * (p - 5) * (p - 6))


def test_change_area_triangle():
    t = Triangle(4, 5, 6)
    f_area = t.area
    t.a = 5
    p = t.perimeter / 2
    assert t.area != f_area and t.area == math.sqrt(p * (p - 5) * (p - 5) * (p - 6))


def test_perimeter_triangle():
    t = Triangle(3, 4, 5)
    assert t.perimeter == 3 + 4 + 5


def test_change_perimeter_triangle():
    t = Triangle(3, 4, 5)
    f_perimeter = t.perimeter
    t.a = 4
    assert t.perimeter != f_perimeter and t.perimeter == 4 + 4 + 5


def test_add_area_triangle():
    t = Triangle(4, 5, 6)
    f_area = t.area
    c = Circle(12)
    try:
        t.add_area(c)
    except ValueError:
        assert False
    assert t.area == f_area + c.area


def test_neg_add_area_triangle():
    t = Triangle(4, 5, 6)
    try:
        t.add_area(13)
        assert False
    except ValueError:
        assert True
