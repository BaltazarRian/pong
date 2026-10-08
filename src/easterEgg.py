import turtle
import time

from objects.Window import Window


def easterEgg(window: Window, window_width: int):
    plane = turtle.Turtle()
    plane.hideturtle()
    plane.penup()
    plane.color("blue")

    # Plane Easter Egg Art
    ascii_art = r"""
                                                            ______
                                                           |  __  \
                                                           | |  \  \
                      _____________________________        | |   \  \
                    /                               \      | |    \  \
   ================|      ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★      |====/ /______\  \_____
   ==              |                                 |===/ _______________   )
   ==              |       JOIN THE AIR FORCE!       |==/ /   _   _   _   / /
   ==              |                                 |=/ /   (_) (_) (_) / /
   ================\________________________________/==\ \______________/ /
                                                        \________________/
                                                           /          /
                                                          /          /
                                                         /__________/
    """

    # Starts far off-screen
    x = -950

    # Flies the plane
    while x < -(window_width / 2 - 100):
        plane.clear()
        plane.goto(x, -90)  # Lowered Y to accommodate the larger art
        plane.write(ascii_art, align="left", font=("Courier", 10, "bold"))

        x += 6  # Slower, smoother glide
        window.update()
        time.sleep(0.05)  # Keep the visual easy to track

    # Note: No plane.clear() here so it remains visible on screen forever!
