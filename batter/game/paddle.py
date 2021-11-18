from game.actor import Actor
from game.point import Point

class Paddle(Actor):

    # Initialization *
    def __init__(self):
        super().__init__()
        self._type = "paddle"
    
