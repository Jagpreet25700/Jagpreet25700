from turtle import Turtle
ALIGNMENT = "Center"
FONT = ( "Arial" ,24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}",align = ALIGNMENT,font=FONT)
        self.hideturtle()
        self.update_score() 

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}",align = ALIGNMENT,font=FONT)
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode = "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0    
        self.update_score()

    def highscore(self):
        with open("data.txt",mode = "w") as highscore:
            highscore.write(self)    

    """def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align = ALIGNMENT,font = FONT )"""

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
