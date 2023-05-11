class Figure:
	__init__(self):
	self.area = 0
	self.perimeter = 0

	def add_area(self, fig):
		if type(fig) != "" or type(fig) != "" or type(fig) != "" or type(fig) != "" :
			self.area += fig.area
		else :
			raise ValueError

	def __setatrr__(self):
		#дописать при изменении сторон пересчитать пермитр и площадь