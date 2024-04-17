import turtle
class Shooter(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.color("green")
        self.shapesize(stretch_wid=3,stretch_len=4)
        self.right(270)
        self.bullets=[]
    def setposition(self,x,y):
        self.penup()
        self.goto(x,y)
    def go_right(self):
        if self.pos()[0] < 370:
            x=self.pos()[0]
            self.setposition(x+30,self.pos()[1])
    def go_left(self):
        if self.pos()[0] > -370:
            x=self.pos()[0]
            self.setposition(x-30,self.pos()[1])
    def getpos(self):
        return [self.pos()[0],self.pos()[1]]
    def shoot(self):
        bullet=turtle.Turtle()
        bullet.shape('circle')
        bullet.color('white')
        bullet.penup()
        bullet.shapesize(stretch_wid=0.5,stretch_len=0.5)
        bullet.setposition(self.pos()[0],self.pos()[1]+0.1)
        self.bullets.append(bullet)
    def move_bullets(self):
        for bullet in self.bullets:
            y=bullet.pos()[1]
            bullet.setposition(bullet.pos()[0],y+5)


    def collision(self, bullets,scoreboard):
        for bullet in bullets:
                if self.distance(bullet) < 10:
                    scoreboard.end_of_game()
                    return False
        return True