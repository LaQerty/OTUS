from figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        self.a = a
        self.area = a * a
        self.perimeter = 4 * a

    def refresh_area(self):
        self.area = self.a * self.a

    def refresh_perimeter(self):
        self.perimeter = 4 * self.a
