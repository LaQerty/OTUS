import Figure from figure
PI = 3.14

class Circle(Figure):
	__init__(self, r: int):
		self.r = r
		self.area = PI * r * r
		self.perimeter = 2 * r * PI