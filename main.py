from turtle import Turtle, Screen
from paddles import Paddles, PADDLES, PADDLES_STARTING_POSITIONS
from ball import Ball
from scoreboard import Scoreboard, SCOREBOARD_STARTING_POSITION
from map import Map
import time

score_player_1 = Scoreboard(SCOREBOARD_STARTING_POSITION[0])
score_player_1.write(arg=score_player_1.current_score, align="center", font=('Courier', 40, 'normal'))
score_player_2 = Scoreboard(SCOREBOARD_STARTING_POSITION[1])
score_player_2 .write(arg=score_player_2.current_score, align="center", font=('Courier', 40, 'normal'))

screen = Screen()  # Create the screen object
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

turtle = Turtle()  # Create the turtle object

board = Map()  # Create the map object

for pos in PADDLES_STARTING_POSITIONS:
    PADDLES.append(Paddles(pos))  # We add a Paddles object to the list of Paddles with the correct position

ball = Ball()

screen.listen()  # Make the screen start accepting inputs
screen.onkey(fun=PADDLES[0].move_up, key="Up")
screen.onkey(fun=PADDLES[0].move_down, key="Down")
screen.onkey(fun=PADDLES[1].move_up, key="w")
screen.onkey(fun=PADDLES[1].move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if abs(ball.ycor()) > 280:
        ball.bounce(object_hit="wall")
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        score_player_1.current_score += 1
        score_player_1.update_score()
        PADDLES[0].goto(PADDLES_STARTING_POSITIONS[0])
        PADDLES[1].goto(PADDLES_STARTING_POSITIONS[1])
        time.sleep(1)
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        score_player_2.current_score += 1
        score_player_2.update_score()
        PADDLES[0].goto(PADDLES_STARTING_POSITIONS[0])
        PADDLES[1].goto(PADDLES_STARTING_POSITIONS[1])
        time.sleep(1)
    for paddle in PADDLES:
        if ball.distance(paddle) < 50 and abs(ball.xcor()) > 320:
            ball.bounce(object_hit="paddle")


screen.exitonclick()
