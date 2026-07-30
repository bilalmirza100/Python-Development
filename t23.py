import time
from turtle import Screen
from t23player import Player
from t23crmngr import CarManager
from t23scrbd import ScoreBoard


screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(player.go_up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_cars()


    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
    if player.is_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()