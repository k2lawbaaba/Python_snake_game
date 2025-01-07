import time
import turtle as tl
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen= tl.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Python Game")
screen.tracer(0)  #turn off display on the screen
screen.listen()

# def fwd():
#     lt(2)
#     fd(10)
snakes= Snake()
foods = Food()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

game_is_on=True
initial_score=0
scoreboard= ScoreBoard(initial_score)
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snakes.move()
    xcor=snakes.snake_head.xcor()
    ycor=snakes.snake_head.ycor()

    snake_dist=snakes.snake_head.distance(foods) #getting the snake and food distance

    # Detecting wall collision
    if xcor > 280 or xcor < -280 or ycor > 270 or ycor < -280:
        game_is_on =False
        scoreboard.game_over()

    # Detecting snake eating the food
    if snake_dist < 15:
        foods.create_food()
        snakes.add_to_snake()
        initial_score +=1
        scoreboard.update_score(initial_score)

    # Detecting snake self collision
    if len(snakes.turtles) > 5:
        for snake in snakes.turtles[1:]:
            if snakes.snake_head.distance(snake) < 10:
                game_is_on =False
                scoreboard.game_over()


screen.exitonclick()