import time
import turtle
import random
from paddle import Player
from ball import Ball

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(760, 1000)
screen.listen()
Bricks = None


def walls():
    global Bricks
    Colors = ['Green', 'Orange', 'Blue', 'Red', 'Yellow', 'Brown', 'Purple', 'Pink']
    x = -340
    y = 480
    Bricks = []
    for t in range(5):
        for i in range(16):
            bricks = turtle.Turtle()
            bricks.penup()
            bricks.shape('square')
            bricks.shapesize(1, 2)
            bricks.sety(y)
            bricks.setx(x)
            bricks.color(random.choice(Colors))
            x += 45
            Bricks.append(bricks)
        x = -340
        y -= 25


walls()

Player_1 = Player()
The_ball = Ball()


screen.tracer(0)
Player_1.move_left()
Player_1.move_right()
screen.onkeypress(Player_1.move_left, 'Left')
screen.onkeypress(Player_1.move_right, 'Right')
speed = 0.1
lives = 3
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    The_ball.move_ball()
    for i in Bricks:
        if i.distance(The_ball) < 55:
            i.hideturtle()
            Bricks.remove(i)
            The_ball.ball_bounce_y()
    if The_ball.xcor() >= 340 or The_ball.xcor() <= -340:
        The_ball.ball_bounce_x()
    if The_ball.distance(Player_1) < 65 and The_ball.ycor() < -460:
        The_ball.ball_bounce_y()

    if The_ball.ycor() > 490:
        The_ball.ball_bounce_y()

    if len(Bricks) <= 0:
        walls()
        speed *= 0.9

    if The_ball.ycor() < -490:
        The_ball.goto(0, -460)
        Player_1.goto(0, -480)
        lives -= 1
        if lives == 0:
            game_is_on = False
        screen.update()
        time.sleep(2)


screen.exitonclick()