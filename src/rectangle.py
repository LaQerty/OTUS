import Figure from figure

class Rectangle(Figure):
	__init__(self, a: int, b: int):
		self.a = a
		self.b = b
		self.area = a * b
		self.perimeter = 2 * a + 2 * b