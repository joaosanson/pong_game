from ball import Ball
from turtle import Screen
from paddle import Paddle
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()


screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "W")
screen.onkeypress(l_paddle.go_down, "S")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision
    if ball.distance(r_paddle) < 80 and ball.xcor() > 320 or ball.distance(l_paddle) < 80 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_increase_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_increase_score()

screen.exitonclick()
