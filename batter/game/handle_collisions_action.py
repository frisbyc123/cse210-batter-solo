from game.constants import SOUND_BOUNCE
from game import audio_service
from game import constants
from game.action import Action
from game.point import Point
from game.physics_service import PhysicsService
from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self.audio_service = AudioService()
        

    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        
        if self._physics_service.is_collision(ball, paddle):
            self.x_velocity = ball._velocity.get_x()
            self.y_velocity = ball._velocity.get_y() * -1
            ball.set_velocity(Point(self.x_velocity, self.y_velocity))
            self.audio_service.play_sound(SOUND_BOUNCE)

        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                self.x_velocity = ball._velocity.get_x()
                self.y_velocity = ball._velocity.get_y() * -1
                ball.set_velocity(Point(self.x_velocity, self.y_velocity))
                self.audio_service.play_sound(SOUND_BOUNCE)
                cast["bricks"].remove(brick)
