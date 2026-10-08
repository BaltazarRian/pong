from enum import Enum

from .BaseObject import BaseObject


class Players(Enum):
    PlayerA = "LeftPaddle"
    PlayerB = "RightPaddle"


# Extends BaseObject to make Ball
class Ball(BaseObject):
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        ball_speed: float,
        stretch_w: int,
        stretch_l: int,
        window_width: int,
        window_height: int,
    ):
        super().__init__(x_pos, y_pos, window_width, window_height)
        self.stretch_w = stretch_w
        self.stretch_l = stretch_l
        self.shapesize(stretch_wid=stretch_w, stretch_len=stretch_l)
        self.shape("square")
        self.dx = ball_speed
        self.dy = ball_speed
        self.window_width = window_width
        self.window_height = window_height

    def _borderCheck(self):
        height_dif = (self.window_height / 2) - (self.stretch_l * 20)
        width_dif = (self.window_width / 2) - (self.stretch_w * 20)

        # Y Border Check
        if self.ycor() > height_dif:
            self.sety(height_dif)
            self.dy *= -1
        elif self.ycor() < -height_dif:
            self.sety(-height_dif)
            self.dy *= -1

        # X Border Check
        if self.xcor() > width_dif:
            self.goto(0, 0)
            self.dx *= -1
            return Players.PlayerB
        elif self.xcor() < -width_dif:
            self.goto(0, 0)
            self.dx *= -1
            return Players.PlayerA

    def setX(self):
        self.setx(self.xcor() + self.dx)
        return self._borderCheck()

    def setY(self):
        self.sety(self.ycor() + self.dy)
        return self._borderCheck()
