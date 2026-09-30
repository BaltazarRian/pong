import turtle

from .Paddle import Paddle
from .Ball import Ball
from .Pen import Pen


# Game Window
class Window:
    def __init__(
        self,
        width: int,
        height: int,
    ):
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width, height)
        self.wn.tracer(0)

    def update(self):
        self.wn.update()

    def listen(self):
        self.wn.listen()

    def onkeypress(self, left_paddle: Paddle, right_paddle: Paddle):
        # Left Paddle Movements
        self.wn.onkeypress(left_paddle.up, "w")
        self.wn.onkeypress(left_paddle.down, "s")

        # Right Paddle Movements
        self.wn.onkeypress(right_paddle.up, "i")
        self.wn.onkeypress(right_paddle.down, "k")
