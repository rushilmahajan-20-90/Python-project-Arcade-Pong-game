from turtle import Turtle
import winsound


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()
       
    def update_scoreboard(self):
        self.clear()
        self.goto(-70,170) 
        self.write(self.l_score,align="center",font=("jokerman",80,"normal"))
        self.goto(70,170)
        self.write(self.r_score,align="center",font=("jokerman",80,"normal")) 
        self.goto(-240,230)
        self.color("#00ffff")
        self.write("PLAYER-1:", align="center", font=("Jokerman", 30, "bold")) 
        self.goto(240, 230)
        self.write(":PLAYER-2", align="center", font=("Jokerman", 30, "bold"))  
        
    def l_point(self):
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        self.l_score+=1
        self.update_scoreboard()
        
    def r_point(self):
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        self.r_score+=1
        self.update_scoreboard()