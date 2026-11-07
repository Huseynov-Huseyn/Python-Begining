from Shape import Shape


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It's a {self.__class__.__name__} with an area of {3.14 * self.radius * self.radius}")
        super().describe()
