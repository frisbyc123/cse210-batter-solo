from game.actor import Actor
from game.point import Point
import random

class Ball(Actor):
    """
    Instance of actor.  Used to track the ball.  Selects a random x velocity at startup, and set the actor type as "ball"
    """

    # initialization *
    def __init__(self):
        super().__init__()
        self._velocity = Point(int(random.randint(-10, 10)), 7)
        self._type = "ball"
