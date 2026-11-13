from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("courier", 18, "normal")
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def update_score(self):
        self.write(f"score:{self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
