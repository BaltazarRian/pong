from .BaseObject import BaseObject


# Extends BaseObject to make Ball
class Ball(BaseObject):
    def __init__(self, x_pos: int, y_pos: int):
        super().__init__(x_pos, y_pos)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
