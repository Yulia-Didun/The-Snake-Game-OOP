from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, 'normal')


class ScoreBoard(Turtle):
    """Class to manage the scoreboard for the game"""
    def __init__(self):
        super().__init__()
        self.score = 0

        # Configure turtle object
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 275)
        self.update_score()

    def update_score(self):
        """Updates the score on the scoreboard"""
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        """Increments the score and updates the scoreboard"""
        self.score += 1
        self.clear()
        self.update_score()

    def game_over_message(self):
        """Displays the 'GAME OVER' message in the center of the screen"""
        self.setpos(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
