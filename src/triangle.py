from figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):
        if a + b < c or a + c < b or b + c < a:
            raise ValueError
        self.a = a
        self.b = b
        self.c = c
        self.perimeter = a + b + c
        p = self.perimeter / 2
        self.area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def refresh_area(self):
        p = self.perimeter / 2
        self.area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def refresh_perimeter(self):
        self.perimeter = self.a + self.b + self.c
