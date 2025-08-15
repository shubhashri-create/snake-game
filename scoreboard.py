from turtle import Turtle
alignment= "center"
font_size= font=("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=alignment, font=font_size)

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=alignment, font=font_size)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

