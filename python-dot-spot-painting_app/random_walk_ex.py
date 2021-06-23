import turtle as t
import random

my_turtle = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(1,255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rgb_color = (r,g,b)

    return rgb_color


direction = [my_turtle.forward(50), my_turtle.backward(50)]
angles = [0, 90, 180, 270]

line_thickness = 2
speed = 1

for _ in range(200):
    print(random_colour())
    my_turtle.speed("fastest")
    my_turtle.color(random_colour())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(angles))
    my_turtle.pensize(15)
    line_thickness += 0.1




screen = Screen()
screen.exitonclick()