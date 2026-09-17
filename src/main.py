from objects.Paddle import Paddle
from objects.Ball import Ball
from objects.Window import Window

# Game Window
wn = Window()

# Left Paddle
left_paddle = Paddle(-350, 0, 5, 1)

# Right Paddle
right_paddle = Paddle(350, 0, 5, 1)

# Ball
ball = Ball(0, 0)

# Main game loop
while True:
    wn.update()
