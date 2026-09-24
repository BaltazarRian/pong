from objects.Paddle import Paddle
from objects.Ball import Ball
from objects.Window import Window

# Left Paddle
left_paddle = Paddle(-350, 0, 5, 1, 20)

# Right Paddle
right_paddle = Paddle(350, 0, 5, 1, 20)

# Ball
ball = Ball(0, 0)

# Game Window
wn = Window(left_paddle, right_paddle, ball)

# Main game loop
while True:
    wn.update()
    wn.listen()
    wn.onkeypress(left_paddle, right_paddle)
