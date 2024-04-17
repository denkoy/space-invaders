FONT = ("Courier", 24, "normal")


from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()

        self.goto(-350, -250)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def plus(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", move=False, align='left', font=('Arial', 24, 'normal'))

    def end_of_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 30, 'normal'))

    def win(self):
        self.goto(0, 0)
        self.write(f"YOU WIN!", move=False, align='center', font=('Arial', 30, 'normal'))
