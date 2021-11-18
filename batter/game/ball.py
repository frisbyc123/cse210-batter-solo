from game.actor import Actor
from game.point import Point
import random

class Ball(Actor):

    # initialization *
    def __init__(self):
        super().__init__()
        self._velocity = Point(int(random.randint(0, 10)), 3)
        self._type = "ball"
