from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1


    def ball_move(self):

        # if self.xcor() > 340:
        #     self.goto(self.xcor(),self.ycor())
        # else:
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x,new_y)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.ball_bounce_x()




