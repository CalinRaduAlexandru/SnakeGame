from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_square = Turtle("square")
        new_square.penup()
        new_square.goto(position)
        new_square.color("white")
        self.square_list.append(new_square)

    def extend(self):
        self.add_segment(self.square_list[-1].position())


    def move(self):
        for new_seg in range(len(self.square_list) - 1, 0, -1):
            new_x = self.square_list[new_seg - 1].xcor()
            new_y = self.square_list[new_seg - 1].ycor()
            self.square_list[new_seg].goto(new_x, new_y)
        self.head.speed(10)
        self.head.forward(MOVE_DISTANCE)

    def turbo(self):
        self.head.forward(40)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)