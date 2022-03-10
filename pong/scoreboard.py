from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.setposition(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))
