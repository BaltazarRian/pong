#!/usr/bin/env python3

import random
from objects.Ball import Ball, Players
from objects.Paddle import Paddle
from objects.Scoreboard import Scoreboard
from objects.Window import Window
from easterEgg import easterEgg

# Constants
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
PADDLE_LENGTH = 1
PADDLE_WIDTH = 5
PADDLE_X_DIST = 350
BALL_SPEED = 0.1

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
    random.choice([-1, 1]),
    random.choice([-1, 1]),
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

# Scoreboard
scoreboard = Scoreboard(WINDOW_HEIGHT)

# Game Window
wn = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
game_active = True
easter_egg = False

# Main game loop
while True:
    try:
        wn.update()

        if game_active:
            wn.listen()
            wn.onkeypress(left_paddle, right_paddle)

            goalCheck = ball.setX()
            ball.setY()

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
            if not easter_egg and (left_paddle.score == 3 or right_paddle.score == 3):
                # Hide the objects
                left_paddle.hideturtle()
                right_paddle.hideturtle()
                ball.hideturtle()
                scoreboard.clear()

                easterEgg(wn, WINDOW_WIDTH)
                easter_egg = True
                game_active = False  # PAUSE GAMEPLAY FOREVER

            # Paddle Collision Logic
            if (ball.xcor() > 340 and ball.xcor() < PADDLE_X_DIST) and (
                ball.ycor() < right_paddle.ycor() + 40
                and ball.ycor() > right_paddle.ycor() - 50
            ):
                ball.setx(340)
                ball.dx *= -1
            elif (ball.xcor() < -340 and ball.xcor() > -PADDLE_X_DIST) and (
                ball.ycor() < left_paddle.ycor() + 40
                and ball.ycor() > left_paddle.ycor() - 50
            ):
                ball.setx(-340)
                ball.dx *= -1
        else:
            # Game is paused/stopped for easterEgg
            pass

    except Exception:
        print("Closed Successfully!")
        break
