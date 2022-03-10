from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.setpos(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
