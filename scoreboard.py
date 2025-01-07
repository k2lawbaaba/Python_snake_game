from turtle import Turtle
FONT=('Arial', 20, 'normal')
ALIGN='center'
class ScoreBoard(Turtle):
    def __init__(self,score):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.teleport(0, 270)
        self.update_score(score)

    def update_score(self,score):
        self.clear()
        self.write(f"Score: {score} ", align=ALIGN, font=FONT)
    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)