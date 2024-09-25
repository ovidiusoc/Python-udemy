from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def generate_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        y = random.randint(-250, 250)
        car.goto(300, y)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)
