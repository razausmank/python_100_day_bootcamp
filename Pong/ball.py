from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, x_position=0, y_position=0):
        super().__init__()
        self.goto(x_position, y_position)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(random.randint(a=0, b=359))
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        print(self.xcor(), self.ycor())


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
