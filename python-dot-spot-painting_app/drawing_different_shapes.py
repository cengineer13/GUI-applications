from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
figure_edges = 3
colours = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]


tim.shape("turtle")
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_sides_n)

screen.exitonclick()