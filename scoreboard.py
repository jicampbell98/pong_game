from turtle import Turtle

SCOREBOARD_STARTING_POSITION = [(-100, 200), (100, 200)]


class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.speed("fastest")
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(score)

    def starting_score(self):
        self.write(arg=self.current_score, align="center", font=('Courier', 40, 'normal'))

    def update_score(self):
        self.clear()
        self.write(arg=self.current_score, align="center", font=('Courier', 40, 'normal'))
