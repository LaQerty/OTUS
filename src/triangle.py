import Figure from figure
import math

class Triangle(Figure):
	__init__(self, a: int, b: int, c: int):
		if a + b < c or a + c < b or b + c < a:
			raise ValueError
		self.a = a
		self.b = b
		self.c = c
		self.perimeter = a + b + c
		p = self.perimeter/2
		self.area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
		