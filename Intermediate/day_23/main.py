import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("The turtle crossing capstone")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")

cyclic_generation = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cyclic_generation += 1
    # generate car
    if cyclic_generation == 6:
        car_manager.generate_car()
        cyclic_generation = 0
    car_manager.move_cars()
    # check collision with cars
    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    # reached the finish line
    if turtle.is_at_finish_line():
        turtle.refresh()
        scoreboard.level_up()
        car_manager.speed_up()

screen.exitonclick()
