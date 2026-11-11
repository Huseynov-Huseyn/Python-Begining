from Predator import Predator
from Prey import Prey


class Fish(Prey, Predator):
    def __init__(self):
        super().__init__()
