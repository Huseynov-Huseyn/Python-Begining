class Circle:
    __match_args__ = ("radius",)

    def __init__(self, radius):
        self.radius = radius


class Rectangle:
    __match_args__ = ("width", "height")

    def __init__(self, width, height):
        self.width = width
        self.height = height


def check_shape(shape):
    match shape:
        case Circle(radius):
            print(f"Circle radius: {radius}")
        case Rectangle(width, height):
            print(f"Rectangle: {width} × {height}")
        case _:
            print("Unknown shape")


check_shape(Circle(10))
check_shape(Rectangle(4, 6))
