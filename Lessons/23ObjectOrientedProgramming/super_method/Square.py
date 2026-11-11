from Shape import Shape


class Square(Shape):
    def __init__(self, color, is_filled, height):
        super().__init__(color, is_filled)
        self.height = height

    def describe(self):
        print(f"It's a {self.__class__.__name__} with an area of {self.height * self.height}")
        super().describe()
