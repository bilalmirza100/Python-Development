from turtle import Turtle, Screen
import random


is_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Color win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race = True


while is_race: 
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lose! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0,10))


screen.exitonclick()