from objects.Paddle import Paddle
from objects.Ball import Ball
from objects.Window import Window

# Constants
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

# Left Paddle
left_paddle = Paddle(-350, 0, 5, 1, 20, WINDOW_WIDTH, WINDOW_HEIGHT)

# Right Paddle
right_paddle = Paddle(350, 0, 5, 1, 20, WINDOW_WIDTH, WINDOW_HEIGHT)

# Ball
ball = Ball(0, 0, 0.1, 0.1, WINDOW_WIDTH, WINDOW_HEIGHT)

# Game Window
wn = Window(WINDOW_WIDTH, WINDOW_HEIGHT, left_paddle, right_paddle, ball)

# Main game loop
while True:
    wn.update()
    wn.listen()
    wn.onkeypress(left_paddle, right_paddle)

    ball.setX()
    ball.setY()
