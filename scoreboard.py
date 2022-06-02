from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-100, y=180)
        self.write(f'{self.l_score}', align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=180)
        self.write(f'{self.r_score}', align=ALIGNMENT, font=FONT)

    def r_increase_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_increase_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
