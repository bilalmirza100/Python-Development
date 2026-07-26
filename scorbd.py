from turtle import Turtle
import random

alignment = "center"
font = ("Calibri", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updt_scrbd()

    def updt_scrbd(self):
        self.write(f"Score : {self.score}", align=alignment, font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=alignment, font=font)

    def increase_scr(self):
        self.score +=1
        self.clear()
        self.updt_scrbd()