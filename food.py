from turtle import Turtle
from random import randint


class Food(Turtle):
    """Class to create a food object that the snake can 'eat'"""
    def __init__(self):
        super().__init__()

        # Set the properties of the food object
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")

        # Call the refresh method to move the food to a random location
        self.refresh()

    def refresh(self):
        # Generate random coordinates within the game screen and move food to them
        new_x = randint(-280, 280)
        new_y = randint(-280, 280)
        self.goto(new_x, new_y)
