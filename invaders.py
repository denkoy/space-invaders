from turtle import Turtle
import random


class Invaders():
    def __init__(self):
        self.invaders=[]
        self.direction='r'
        self.invaders_bullets=[]
    def add_invaders(self):
        x = [-80, -40, 0, 40, 80]
        for j in x:
            y = [280, 250, 220, 190, 160, 130]
            for i in y:
                #purvo nai gore lqvo posle nakraq nai dolu dqqsno
                temp = Turtle("turtle")
                temp.color("green")
                temp.penup()
                temp.right(90)
                temp.shapesize(stretch_len=1, stretch_wid=1)
                temp.setposition(j, i)
                self.invaders.append(temp)

    def move(self):
        if self.direction=='r':
            if self.invaders[len(self.invaders)-1].pos()[0]<370:
                for i in self.invaders:
                    i.setposition(i.pos()[0]+1,i.pos()[1])
            else:
                self.direction='l'
        elif self.direction=='l':
            if self.invaders[0].pos()[0]>-370:
                for i in self.invaders:
                    i.setposition(i.pos()[0]-1,i.pos()[1])
            else:
                self.direction='r'
    def collision(self, bullets,scoreboard):
        for bullet in bullets:
            for invader in self.invaders:
                if invader.distance(bullet) < 10:
                    invader.reset()
                    self.invaders.remove(invader)
                    bullet.reset()
                    bullets.remove(bullet)
                    scoreboard.plus()
                    return True
        return False
    def shoot(self):
        for i in self.invaders:
            integer=random.randint(1,len(self.invaders)*16)
            if integer == 100:
                bullet = Turtle()
                bullet.shape('arrow')
                bullet.color('red')
                bullet.penup()
                bullet.right(90)
                bullet.shapesize(stretch_wid=0.45, stretch_len=0.45)
                bullet.setposition(i.pos()[0], i.pos()[1] + 0.7)
                self.invaders_bullets.append(bullet)

    def move_bullets(self):
        for bullet in self.invaders_bullets:
            y = bullet.pos()[1]
            bullet.setposition(bullet.pos()[0], y - 2)
