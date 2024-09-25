from turtle import Turtle, Screen
import random

WIDTH = 500
HEIGHT = 400

is_race_on = False
screen = Screen()

screen.setup(width=WIDTH, height=HEIGHT)
screen.listen()
title = "Make your bet"
prompt = "Who will win the race? Enter a color"
bet = screen.textinput(title=title, prompt=prompt)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

yaxis = -60
for items in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(items)
    new_turtle.goto(x=-240, y=yaxis)
    turtles.append(new_turtle)
    yaxis += 20

if bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 220:
            is_race_on = False
            turtle_winner = turtle.pencolor()
            break
if bet == turtle_winner:
    print("You win!")
else:
    print("You lose!")
print(turtle_winner)


# screen.onkey(key="w", fun=move_forward)
screen.exitonclick()

