import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")

def change_color(tartaruga):
    R = random.randrange(0,256)
    G = random.randrange(0,256)
    B = random.randrange(0,256)
    tartaruga.color(R, G, B)

def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)


def draw(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        change_color(tim)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw(10)


screen = Screen()
screen.exitonclick()