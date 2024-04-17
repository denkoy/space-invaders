from scoreboard import Scoreboard
from turtle import Turtle,Screen
from shooter import Shooter
from invaders import Invaders
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.listen()
game_is_on = True
screen.listen()

invaders=Invaders()
invaders.add_invaders()
arrow = Shooter()
arrow.setposition(0,-230)
screen.onkey(arrow.go_right,"Right")
screen.onkey(arrow.go_left,"Left")
screen.onkey(arrow.shoot,'space')
scoreboard=Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.03)
    if len(invaders.invaders) == 0:
        scoreboard.win()
        break

    arrow.move_bullets()
    invaders.move()
    invaders.collision(arrow.bullets,scoreboard)
    invaders.shoot()
    invaders.move_bullets()
    if not arrow.collision(invaders.invaders_bullets,scoreboard):
        game_is_on=False



screen.exitonclick()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
