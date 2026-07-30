from turtle import Turtle



FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scrbd()


    def update_scrbd(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level +=1
        self.update_scrbd()