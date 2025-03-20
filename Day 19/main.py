from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def setup_position():
    tim.penup()
    tim.goto(-200,-200)
    tim.pendown()

def move_forwards():
    tim.forward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def move_backwards():
    tim.backward(10)
def delete_everything():
    tim.reset()
    setup_position()

setup_position()
screen.listen()
screen.onkey(key ="w", fun=move_forwards)
screen.onkey(key ="s", fun=move_backwards)
screen.onkey(key ="a", fun=turn_left)
screen.onkey(key ="d", fun=turn_right)
screen.onkey(key ="c", fun=delete_everything)

screen.exitonclick()