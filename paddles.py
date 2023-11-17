from turtle import Turtle
PADDLES_STARTING_POSITIONS = [(350, 0), (-350, 0)]
PADDLES = []


class Paddles(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)  # Stretch the 20x20 pixel square 5 times vertically (20x100)
        self.goto(pos)
        self.lower_end = self.ycor() - 50
        self.upper_end = self.ycor() + 50

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
