from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.goto(x_cor, y_cor)
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

