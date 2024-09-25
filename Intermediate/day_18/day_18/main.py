from turtle import Screen
import turtle as t
import random

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

def square(object):
    for _ in range(4):
        object.forward(50)
        object.left(90)


def dashed_line(object):
    object.forward(10)
    object.penup()
    object.forward(10)
    object.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t.colormode(255)
directions = [0, 90, 180, 270]
timmy = t.Turtle()
timmy.shape("circle")
timmy.speed("fastest")
num_circles = int(input("Insert the number of circles: "))
angle = 360/num_circles
for _ in range(num_circles):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(angle)

# for _ in range(200):
#     timmy.color(random_color())
#     direction = random.choice(directions)
#     timmy.setheading(direction)
#     timmy.forward(30)


screen = Screen()
screen.exitonclick()
