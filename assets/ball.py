from turtle import Turtle,addshape
import random
import winsound 


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        addshape("ball.gif")
        self.shape("ball.gif")
        self.penup()
        self.x_move=10#for bounce
        self.y_move=10#for bounce
        self.move_speed=0.1#to increase ball speed
        
        
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
        self.y_move *=-1
        
    def bounce_x(self):
        winsound.PlaySound("paddle.wav",winsound.SND_ASYNC)
        self.x_move*=-1
        self.move_speed = max(self.move_speed*0.9,0.02)## Invert horizontal direction and slightly increase speed (i.e. make move_speed smaller).Also cap the minimum move_speed so the ball doesn't become impossibly fast. 

        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.x_move = 10 * random.choice((1, -1))
        # give a small random vertical angle so gameplay is varied
        self.y_move = random.choice((6, 8, 10, -6, -8, -10))
        