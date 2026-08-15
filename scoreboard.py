from linecache import updatecache
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.curr_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(align=ALIGNMENT, font=FONT, arg=f"Score: {self.curr_score}     High Score: {self.high_score}")

    def reset(self):
        if self.curr_score > self.high_score:
            self.high_score = self.curr_score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.curr_score = 0
        self.update_score()

    def increase_score(self):
        self.curr_score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)


