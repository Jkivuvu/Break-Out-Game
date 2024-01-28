from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        self.move = 0
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 8)
        self.setx(self.move)
        self.sety(-480)
        self.color('white')


    def move_right(self):
        if self.xcor() != 320:
            self.move += 20
            self.setx(self.move)
        else:
            pass


    def move_left(self):
        if self.xcor() != -320:
            self.move -= 20
            self.setx(self.move)
        else:
            pass


