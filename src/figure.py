class Figure:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def refresh_area(self):
        self.area = 0

    def refresh_perimeter(self):
        self.perimeter = 0

    def add_area(self, fig):
        if isinstance(fig, Figure):
            self.area += fig.area
        else:
            raise ValueError

    def __setattr__(self, name, value):
        keys = list(self.__dict__.keys())
        if name in keys:
            if name != "area" and name != "perimeter":
                self.__dict__[name] = value
                self.refresh_perimeter()
                self.refresh_area()
            else:
                self.__dict__[name] = value
        else:
            self.__dict__[name] = value
