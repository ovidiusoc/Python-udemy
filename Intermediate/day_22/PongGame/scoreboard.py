from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
POSITION = (0, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_left}   {self.score_right}", align=ALIGNMENT, font=FONT)

    def add_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_score()

    def add_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_score()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"GAME OVER! {winner} player wins?", align=ALIGNMENT, font=FONT)

    def check_score(self):
        result = True
        if self.score_left == 5:
            self.game_over("Left")
            result = False
        if self.score_right == 5:
            self.game_over("Right")
            result = False
        return result
