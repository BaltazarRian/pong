from .BaseObject import BaseObject


# Extends BaseObject to make Paddles
class Paddle(BaseObject):
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        length: int,
    ):
        super().__init__(x_pos, y_pos)
        self.shapesize(stretch_wid=width, stretch_len=length)
