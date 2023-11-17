def bounce_checker(self, paddle_ends, paddle_x):
    lower_bound, upper_bound = paddle_ends
    if abs(self.xcor()) > 390 or abs(self.ycor()) > 300:  # Ball has hit an upper or lower wall
        self.bounce("wall")
    elif lower_bound <= self.ycor() <= upper_bound and abs(self.xcor() - paddle_x) < 20:  # Ball has hit a paddle
        self.bounce("paddle")
    else:  # No wall or paddle hit, no change in direction
        self.bounce("no bounce")