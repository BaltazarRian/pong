import turtle


# Base Object for Ball and Paddle
class BaseObject(turtle.Turtle):
    def __init__(self, x_pos: int, y_pos: int):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)
