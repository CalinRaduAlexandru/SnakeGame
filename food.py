from turtle import Turtle, Screen, time
import random

screen = Screen()

colors = [ "red", "blue", "green", "yellow", "pink", "orange", "grey"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.7, stretch_wid = 0.7)
        self.color(colors[random.randint(0, 6)])
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        screen.update()
        self.goto(random_x, random_y)


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(colors[random.randint(0, 6)])
