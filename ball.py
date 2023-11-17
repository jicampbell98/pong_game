from turtle import Turtle
import random

SIDE = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=0)
        self.starting_ball()
        self.x_move = 20
        self.y_move = 20
        self.is_ball_moving = True

    def starting_ball(self):
        self.setheading(random.choice(SIDE))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, object_hit):
        if object_hit == "wall":
            self.y_move *= -1
        elif object_hit == "paddle":
            self.x_move *= -1
