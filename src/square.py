import Figure from figure

class Square(Figure):
	__init__(self, a: int):
		self.a = a
		self.area = a * a
		self.perimeter = 4 * a