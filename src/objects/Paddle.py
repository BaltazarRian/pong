from .BaseObject import BaseObject


# Extends BaseObject to make Paddles
class Paddle(BaseObject):
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        length: int,
        dist: int,
        window_width: int,
        window_height: int,
    ):
        super().__init__(x_pos, y_pos, window_width, window_height)
        self.score = 0
        self.shape("square")
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.dist = dist

    # Up Function
    def up(self):
        y = self.ycor()
        y += self.dist
        self.sety(y)

    # Down Function
    def down(self):
        y = self.ycor()
        y -= self.dist
        self.sety(y)
