from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE_POSITION = (360, 0)
LEFT_PADDLE_POSITION = (-360, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with floor or ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score += 1
        scoreboard.update_score()

    # detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score += 1
        scoreboard.update_score()

    if scoreboard.left_score == 5 or scoreboard.right_score == 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
