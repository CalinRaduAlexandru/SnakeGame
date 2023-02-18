from turtle import Turtle

SCORE = 0
ALIGN = "center"
SCORE_FONT = ("courier", 16, "normal")
GAMEOVER_FONT = ("arial", 32, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()


    def update_score(self):
        self.write(f"YOUR SCORE: {self.score}", align=ALIGN, font=SCORE_FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=GAMEOVER_FONT)

    def reset(self):
        self.screen.reset()



