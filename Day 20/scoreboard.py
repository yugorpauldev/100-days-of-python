from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("data.txt",mode="r") as file:
    score = file.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score =int(score)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as file2:
            file2.write(str(self.high_score))


