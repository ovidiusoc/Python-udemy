from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from turtle import Turtle, Screen
import time

POSITION_RIGHT_PADDLE = (350, 0)
POSITION_LEFT_PADDLE = (-350, 0)

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)


# create the 2 players
r_paddle = Paddle(POSITION_RIGHT_PADDLE)
l_paddle = Paddle(POSITION_LEFT_PADDLE)

# create the ball
ball = Ball()
# create the scoreboard
scoreboard = Scoreboard()

# define the key control
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    # Collision of the ball with a wall and bounce back
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Collision of a paddle with a ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # paddle missing ball
    if ball.xcor() >= 380:
        scoreboard.add_score_left()
        ball.refresh()
        ball.bounce_x()
    if ball.xcor() <= -380:
        scoreboard.add_score_right()
        ball.refresh()
        ball.bounce_x()

    # End the game
    game_is_on = scoreboard.check_score()

    ball.move()


screen.exitonclick()
