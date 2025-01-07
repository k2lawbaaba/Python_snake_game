from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        xcor=random.randrange(270)
        ycor=random.randrange(260)
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5, 1)
        self.color('red')
        self.teleport(xcor, ycor)
