from .BaseObject import BaseObject


# Extends BaseObject to make Paddles
class Paddle(BaseObject):
    def __init__(self, x_pos: int, y_pos: int, width: int, length: int, dist: int):
        super().__init__(x_pos, y_pos)
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
