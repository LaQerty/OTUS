from figure import Figure

PI = 3.14


class Circle(Figure):
    def __init__(self, r: int):
        self.r = r
        self.area = PI * r * r
        self.perimeter = 2 * r * PI

    def refresh_area(self):
        self.area = PI * self.r * self.r

    def refresh_perimeter(self):
        self.perimeter = 2 * self.r * PI
