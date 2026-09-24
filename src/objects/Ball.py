from .BaseObject import BaseObject


# Extends BaseObject to make Ball
class Ball(BaseObject):
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        dx: float,
        dy: float,
        window_width: int,
        window_height: int,
    ):
        super().__init__(x_pos, y_pos, window_width, window_height)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("square")
        self.dx = dx
        self.dy = dy
        self.window_width = window_width
        self.window_height = window_height

    def _borderCheck(self):
        height_dif = 290
        width_dif = 390

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
        elif self.xcor() < -width_dif:
            self.goto(0, 0)
            self.dx *= -1

    def setX(self):
        self.setx(self.xcor() + self.dx)
        self._borderCheck()

    def setY(self):
        self.sety(self.ycor() + self.dy)
        self._borderCheck()
