import turtle

from .Paddle import Paddle


class Scoreboard(turtle.Turtle):
    def __init__(self, screen_height: int):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(
            "Player A: 0 Player B: 0",
            align="center",
            font=("Courier", 24, "normal"),
        )

    def updateScores(self, left_paddle: Paddle, right_paddle: Paddle):
        self.clear()
        self.write(
            f"Player A: {left_paddle.score} Player B: {right_paddle.score}",
            align="center",
            font=("Courier", 24, "normal"),
        )
