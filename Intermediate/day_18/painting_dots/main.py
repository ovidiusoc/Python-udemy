# get the colors from a picture
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_t = (r, g, b)
#     rgb_colors.append(color_t)
#
# print(rgb_colors)
from turtle import Screen
import turtle as t
import random

Number_OF_DOTS = 10
DISTANCE_BETWEEN_DOTS = 50
DOT_SIZE = 20

rgb_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def set_new_psosition(object, axis):
    if axis == "x":
        object.setx(object.xcor() + DISTANCE_BETWEEN_DOTS)
    elif axis == "y":
        object.sety(object.ycor() + DISTANCE_BETWEEN_DOTS)
        object.setx(0)

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.shape("circle")
screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
tim.setpos(0, 10)
tim.penup()
tim.hideturtle()
for _ in range(10):
    for _ in range(10):
        color = random.choice(rgb_colors)
        tim.dot(20, color)
        set_new_psosition(tim,"x")
    set_new_psosition(tim, "y")


screen.exitonclick()

