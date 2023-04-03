from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.move_up, key='Up')
screen.onkey(fun=snake.move_down, key='Down')
screen.onkey(fun=snake.move_left, key='Left')
screen.onkey(fun=snake.move_right, key='Right')

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        score_board.add_score()
        food.refresh()
        snake.extend_snake()

    if snake.check_collision_with_wall():
        game_over = True
        score_board.game_over_message()

    if snake.check_collision_with_tail():
        game_over = True
        score_board.game_over_message()

screen.exitonclick()
