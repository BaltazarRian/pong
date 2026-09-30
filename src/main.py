from objects.Paddle import Paddle
from objects.Ball import Ball, Players
from objects.Scoreboard import Scoreboard
from objects.Window import Window

# Constants
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
PADDLE_LENGTH = 1
PADDLE_WIDTH = 5
PADDLE_X_POS_DIST = 350
BALL_SPEED = 0.075

# Left Paddle
left_paddle = Paddle(
    -PADDLE_X_POS_DIST, 0, PADDLE_WIDTH, PADDLE_LENGTH, 20, WINDOW_WIDTH, WINDOW_HEIGHT
)

# Right Paddle
right_paddle = Paddle(
    PADDLE_X_POS_DIST, 0, PADDLE_WIDTH, PADDLE_LENGTH, 20, WINDOW_WIDTH, WINDOW_HEIGHT
)

# Ball
ball = Ball(0, 0, BALL_SPEED, 1, 1, WINDOW_WIDTH, WINDOW_HEIGHT)

# Scoreboard
scoreboard = Scoreboard(WINDOW_HEIGHT)

# Game Window
wn = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

# Main game loop
while True:
    wn.update()
    wn.listen()
    wn.onkeypress(left_paddle, right_paddle)

    goalCheck = ball.setX()
    ball.setY()

    # Checks for if a player scores
    if goalCheck is Players.PlayerA:
        left_paddle.addScore()
        scoreboard.updateScores(left_paddle, right_paddle)
    elif goalCheck is Players.PlayerB:
        right_paddle.addScore()
        scoreboard.updateScores(left_paddle, right_paddle)

    # Paddle Collision Logic
    if (ball.xcor() > 340 and ball.xcor() < PADDLE_X_POS_DIST) and (
        ball.ycor() < right_paddle.ycor() + 40
        and ball.ycor() > right_paddle.ycor() - 50
    ):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -PADDLE_X_POS_DIST) and (
        ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 50
    ):
        ball.setx(-340)
        ball.dx *= -1
