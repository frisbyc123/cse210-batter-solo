from game.actor import Actor
from game.point import Point

class Ball(Actor):

    # initialization *
    def __init__(self):
        super().__init__()
        self._velocity = Point(5, 5)
        self._type = "ball"
