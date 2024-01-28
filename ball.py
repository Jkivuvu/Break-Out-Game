from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.goto(0, -460)
        self.color('grey')
        self.move_y = 10
        self.move_x = 10

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def ball_bounce_y(self):
        self.move_y *= -1
        self.move_ball()

    def ball_bounce_x(self):
        self.move_x *= -1
        self.move_ball()
