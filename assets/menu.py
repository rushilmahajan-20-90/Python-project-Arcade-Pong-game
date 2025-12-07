from turtle import Turtle,Screen 

class Menu(Turtle):
    def __init__(self):
        super().__init__()
        screen=Screen()
        screen.title("Pong")
        screen.setup(width=800, height=600)
        screen.bgpic("menubackground.png")
        
        self.color("#FF1744")
        self.hideturtle()
        self.penup()
        self.goto(0,100)
        self.write("🏓 PONG GAME 🏓", align="center", font=("Ravie", 40, "bold"))
        self.goto(0,-20)
        self.color("#00FF66")
        self.write("Press SPACE to Start", align="center", font=("Ravie", 20, "normal"))
        self.goto(0,-60)
        self.write("Press Q to Quit", align="center", font=("Ravie", 18, "normal"))
        
        self.goto(-160,-280)
        self.color("#FFD700")
        self.write("Developed by :-- Team-Arcade Legends",align="center",font=("Harrington",20,"normal"))