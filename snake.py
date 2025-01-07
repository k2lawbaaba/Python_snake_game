from turtle import Turtle
X_AXIS = [0, -10, -20]
MOVING_SNAKE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_turtle()
        self.snake_head=self.turtles[0]

    def create_turtle(self):
        for x in range(0, 3):
            jointed_turtles =Turtle("square")
            jointed_turtles.color("white")
            jointed_turtles.pu()
            # jointed_turtles.shapesize(0.7, 0.7,1)
            jointed_turtles.speed("fastest")
            jointed_turtles.goto(x=X_AXIS[x], y=0)
            self.turtles.append(jointed_turtles)
    def add_to_snake(self):
        jointed_turtles = Turtle("square")
        jointed_turtles.color("white")
        jointed_turtles.pu()
        jointed_turtles.speed("fastest")
        # jointed_turtles.goto(x=self.turtles[-1].xcor() - 10, y=0)
        self.turtles.append(jointed_turtles)
    def move(self):
        for x in range(len(self.turtles) - 1, 0, -1):
            xcor = self.turtles[x - 1].xcor()
            ycor = self.turtles[x - 1].ycor()
            self.turtles[x].goto(xcor, ycor)
        # self.snake_head.shape("arrow")
        self.snake_head.fd(MOVING_SNAKE)


    def up(self):
        if self.snake_head.heading() !=DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() !=LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)