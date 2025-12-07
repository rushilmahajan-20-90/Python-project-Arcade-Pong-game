from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from menu import Menu
import winsound
import time
import random

#For Screen
screen=Screen()
screen.title("Pong")
screen.setup(width=800,height=600)
half_width=400#half of screen width used for paddle
screen.bgcolor("#020417")

#For sound
sound_on=True
screen.addshape("soundon.gif")
screen.addshape("soundoff.gif")
sound_icon=Turtle()
sound_icon.penup()
sound_icon.goto(350,250)
sound_icon.shape("soundon.gif")

#For Menu
menu=Menu()
game_is_on=False

#From here main game starts
def start_game():
    global game_is_on
    menu.clear()
    screen.bgpic("")           #  remove background image
    screen.bgcolor("#020417") #  revert to black color
    game_is_on=True
screen.listen()
screen.onkeypress(start_game,"space")
screen.onkeypress(screen.bye,"q")
while not game_is_on:
    screen.update()

 

# Draw center line
center_line = Turtle()
center_line.color("white")
center_line.hideturtle()
center_line.penup()
center_line.goto(0, 300)
center_line.setheading(270)#by default our turtle faces right direction so we have to change its direction . 
center_line.pensize(3)
center_line.speed("fastest")

for _ in range(15):
    center_line.pendown()
    center_line.forward(20)
    center_line.penup()
    center_line.forward(20)
    

screen.tracer(0)


r_paddle=Paddle((half_width-20,0))
l_paddle=Paddle((-half_width+20,0))
ball=Ball()
scoreboard=Scoreboard()


#Paddle controlls
screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


#Updates the screen
while not game_is_on:
    screen.update()
    
    
while game_is_on:
    time.sleep(ball.move_speed*0.6)
    screen.update()
    ball.move()
    


#For ball and paddle collision

    if ball.ycor()>280 or ball.ycor()<-280: #now it needs to buy
        ball.bounce_y()
        
        # Paddle collision (simple clamp + bounce)
    if (ball.distance(r_paddle) < 50 and ball.xcor() > r_paddle.xcor() - 20) \
        or (ball.distance(l_paddle) < 50 and ball.xcor() < l_paddle.xcor() + 20):

    # move the ball just outside the paddle so it can't get stuck inside
        if ball.xcor() > 0:
        # right paddle: place the ball just left of paddle
            paddle=r_paddle
            ball.setx(r_paddle.xcor() - 21)
        else:
        # left paddle: place the ball just right of paddle
            paddle=l_paddle
            ball.setx(l_paddle.xcor() + 21)
            
        
        
        
        # ⭐ SPIN: adjust ball angle based on where it hits the paddle
        offset = ball.ycor() - paddle.ycor()        # how far from paddle center
        ball.y_move = 0.3 * offset

        ball.bounce_x()
 
    



# if r_paddle and l_paddle misses
    if ball.xcor() > half_width - 5:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -half_width + 5:
        ball.reset_position()
        scoreboard.r_point()
        
        
        
    

def toggle_sound(x,y):
    global sound_on
    sound_on=not sound_on
    
    if sound_on:
        sound_icon.shape("soundon.gif")
    else:
        sound_icon.shape("soundoff.gif")
        
    print("Sound:", "ON" if sound_on else "OFF")
    
sound_icon.onclick(toggle_sound)






screen.exitonclick()


