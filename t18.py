import turtle as turtle_module
import random

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors_list = [(140, 78, 53), (187, 164, 121), (52, 111, 136), (164, 153, 40), (17, 44, 79), (140, 60, 85), (140, 170, 177), (63, 119, 100), (146, 183, 173), (84, 33, 27), (218, 210, 102), (65, 153, 167), (112, 39, 31), (164, 100, 130), (101, 145, 114), (167, 144, 161), (92, 122, 171), (176, 105, 86), (64, 44, 53), (36, 55, 102), (207, 182, 195), (100, 44, 56), (172, 201, 194), (166, 203, 207), (22, 95, 79), (219, 179, 174)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101


for i in range(1, number_of_dots):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()