from turtle import Turtle


class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.penup()
        self.color("white")
        self.write(arg="SCORE", align="center", font=('Courier', 25, 'normal'))
        self.draw_board()

    def draw_board(self):
        self.setheading(270)
        for i in range(13):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()
