import turtle


class Window:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

    def update(self):
        self.wn.update()
