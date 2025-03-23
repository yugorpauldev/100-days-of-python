import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height= 600, width = 800)
screen.bgpic("liam.gif")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(360,0)
paddle_2 = Paddle(-360,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.up,key="Up")
screen.onkey(paddle_1.down,key="Down")
screen.onkey(paddle_2.up,key="w")
screen.onkey(paddle_2.down,key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()

    #Detect collision with ball
    if ball.distance(paddle_1) < 40 and ball.xcor() > 340 or ball.distance(paddle_2) < 40 and ball.xcor() < - 340:
        ball.ball_bounce_x()

    #Detect Out of bound

    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.r_point()




screen.exitonclick()