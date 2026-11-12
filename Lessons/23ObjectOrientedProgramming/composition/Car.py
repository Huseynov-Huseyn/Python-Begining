from Engine import Engine
from Wheels import Wheels


class Car:
    def __init__(self, brand):
        self.brand = brand
        # Car combines objects by making one class contain an object of another class. (Composition)
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        return f"{self.brand}: {self.engine.start()} and {self.wheels.rotate()}"
