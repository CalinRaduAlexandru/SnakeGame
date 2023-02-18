from turtle import Turtle, Screen, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

snake = Snake()
food = Food()
score = Scoreboard()

screen.title("SNAKE")
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.turbo, "d")

game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    for segment in snake.square_list[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()









screen.exitonclick()
