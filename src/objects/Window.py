import turtle

from .Paddle import Paddle
from .Ball import Ball


# Game Window
class Window:
    def __init__(self, left_paddle: Paddle, right_paddle: Paddle, ball: Ball):
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

    def update(self):
        self.wn.update()

    def listen(self):
        self.wn.listen()

    def onkeypress(self, left_paddle, right_paddle):
        self.wn.onkeypress(left_paddle.up, "w")
        self.wn.onkeypress(left_paddle.down, "s")

        self.wn.onkeypress(right_paddle.up, "i")
        self.wn.onkeypress(right_paddle.down, "k")
