import turtle

from .Paddle import Paddle


class Scoreboard(turtle.Turtle):
    def __init__(self, screen_height: int, left_paddle: Paddle, right_paddle: Paddle):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.right_paddle = right_paddle
        self.left_paddle = left_paddle
        self.write(
            f"{right_paddle.name}: {right_paddle.score} {left_paddle.name}: {left_paddle.score}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    def updateScores(self):
        self.clear()
        self.write(
            f"{self.right_paddle.name}: {self.right_paddle.score} {self.left_paddle.name}: {self.left_paddle.score}",
            align="center",
            font=("Courier", 24, "normal"),
        )
