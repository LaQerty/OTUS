from figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.area = a * b
        self.perimeter = 2 * a + 2 * b

    def refresh_area(self):
        self.area = self.a * self.b

    def refresh_perimeter(self):
        self.perimeter = 2 * self.a + 2 * self.b
