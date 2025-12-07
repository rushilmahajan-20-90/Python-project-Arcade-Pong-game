from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,Position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(Position)
    def go_up(self):
        new_y=self.ycor()+30
        top_limit=260
        if new_y>top_limit:
            new_y=top_limit
        self.goto(self.xcor(),new_y)
    
    
    def go_up(self):
        new_y = self.ycor() + 30
        top_limit = 260  
        if new_y > top_limit:
            new_y = top_limit
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        bottom_limit = -260
        if new_y < bottom_limit:
            new_y = bottom_limit
        self.goto(self.xcor(), new_y)
