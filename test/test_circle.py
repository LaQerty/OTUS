from circle import Circle
from rectangle import Rectangle
import pytest

PI = 3.14


def test_init_circle():
    c1 = Circle(12)
    assert c1.r == 12


def test_area_circle():
    c1 = Circle(4)
    assert c1.area == PI * 4 * 4


def test_change_area_circle():
    c1 = Circle(4)
    f_area = c1.area
    c1.r = 5
    assert c1.area != f_area 
    assert c1.area == PI * 5 * 5


def test_perimeter_circle():
    c1 = Circle(4)
    assert c1.perimeter == 2 * 4 * PI


def test_change_perimeter_circle():
    c1 = Circle(4)
    f_perimeter = c1.perimeter
    c1.r = 5
    assert c1.perimeter != f_perimeter 
    assert c1.perimeter == 2 * 5 * PI


def test_add_area_circle():
    c1 = Circle(4)
    f_area = c1.area
    r = Rectangle(12, 23)
    c1.add_area(r)
    assert c1.area == f_area + r.area


def test_neg_add_area_circle():
    c1 = Circle(4)
    with pytest.raises(ValueError):
        c1.add_area(13)
