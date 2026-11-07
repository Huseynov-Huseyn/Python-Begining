from Shape import Shape


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It's a {self.__class__.__name__} with an area of {self.height * self.width / 2}")
        super().describe()
