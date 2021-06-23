from turtle import Screen
import turtle as t
import random


jack = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color = (r,g,b)
    return color

angle = 2

while True:
    jack.color(random_colour())
    jack.speed(0)
    jack.circle(100)
    jack.left(angle)
    angle += 5
    if angle == 360:
        break

screen = Screen()

screen.exitonclick()