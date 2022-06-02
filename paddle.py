from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super(Paddle, self).__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(pos)
        self.x = pos[0]
        self.y = pos[1]

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x, new_y)

    def go_down(self):

        new_y = self.ycor() - 20
        self.goto(self.x, new_y)
