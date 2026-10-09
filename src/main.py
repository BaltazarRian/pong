#!/usr/bin/env python3

import random
import time

from easterEgg import easterEgg
from objects.Ball import Ball, Players
from objects.Paddle import Paddle
from objects.Scoreboard import Scoreboard
from objects.Window import Window

# Constants
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
PADDLE_LENGTH = 1
PADDLE_WIDTH = 5
PADDLE_X_DIST = 350
BALL_SPEED = 1
WIN_CONDITION = 3

# Left Paddle
left_paddle = Paddle(
    -PADDLE_X_DIST, 0, PADDLE_WIDTH, PADDLE_LENGTH, 20, WINDOW_WIDTH, WINDOW_HEIGHT
)

# Right Paddle
right_paddle = Paddle(
    PADDLE_X_DIST, 0, PADDLE_WIDTH, PADDLE_LENGTH, 20, WINDOW_WIDTH, WINDOW_HEIGHT
)

# Ball
ball = Ball(
    0,
    0,
    BALL_SPEED,
    1,
    1,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)
# Randomize starting direction
ball.dx = random.choice([-BALL_SPEED, BALL_SPEED])
ball.dy = random.choice([-BALL_SPEED, BALL_SPEED])

# Scoreboard
scoreboard = Scoreboard(WINDOW_HEIGHT)

# Game Window
wn = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
game_active = True
easter_egg = False

# Boundary Calculations (BaseObject size is 20px)
paddle_half_w = (PADDLE_LENGTH * 20) / 2
paddle_half_h = (PADDLE_WIDTH * 20) / 2

# Main game loop
while True:
    try:
        wn.update()
        time.sleep(0.01)

        if game_active:
            wn.listen()
            wn.onkeypress(left_paddle, right_paddle)

            goalCheck = ball.setX()
            ball.setY()

            right_front_x = right_paddle.xcor() - paddle_half_w
            left_front_x = left_paddle.xcor() + paddle_half_w

            # Right Paddle Collision
            if (
                ball.xcor() >= right_front_x and ball.xcor() <= right_paddle.xcor()
            ) and (
                ball.ycor() <= right_paddle.ycor() + paddle_half_h
                and ball.ycor() >= right_paddle.ycor() - paddle_half_h
            ):
                ball.setx(right_front_x)
                ball.dx *= -1

            # Left Paddle Collision
            elif (
                ball.xcor() <= left_front_x and ball.xcor() >= left_paddle.xcor()
            ) and (
                ball.ycor() <= left_paddle.ycor() + paddle_half_h
                and ball.ycor() >= left_paddle.ycor() - paddle_half_h
            ):
                ball.setx(left_front_x)
                ball.dx *= -1

            # Checks for if a player scores
            if goalCheck is Players.PlayerA:
                left_paddle.addScore()
                scoreboard.updateScores(left_paddle, right_paddle)
                ball.dx = random.choice([-BALL_SPEED, BALL_SPEED])
                ball.dy = random.choice([-BALL_SPEED, BALL_SPEED])
            elif goalCheck is Players.PlayerB:
                right_paddle.addScore()
                scoreboard.updateScores(left_paddle, right_paddle)
                ball.dx = random.choice([-BALL_SPEED, BALL_SPEED])
                ball.dy = random.choice([-BALL_SPEED, BALL_SPEED])

            # Trigger easter egg at 3 points
            if not easter_egg and (
                left_paddle.score == WIN_CONDITION
                or right_paddle.score == WIN_CONDITION
            ):
                # Hide the objects
                left_paddle.hideturtle()
                right_paddle.hideturtle()
                ball.hideturtle()
                scoreboard.clear()

                easterEgg(wn, WINDOW_WIDTH)
                easter_egg = True
                game_active = False  # PAUSE GAMEPLAY FOREVER
        else:
            # Pause game for easterEgg
            pass

    except Exception:
        # Close gracefully regardless of what happens
        print("Closed Successfully!")
        break
