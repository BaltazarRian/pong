import turtle


# Base Object for Ball and Paddle
class BaseObject(turtle.Turtle):
    def __init__(self, x_pos: int, y_pos: int, window_width: int, window_height: int):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)
        self.height = window_height
        self.width = window_width
