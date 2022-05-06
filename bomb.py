from vector import Vector
from turtle import Turtle
from border import Border
import random

class Bomb:

    def __init__(self, pos=Vector(0, 0), border=Border(width=550, height=550), speed=2):
        """
        A Bomb object initialized with three properties
        :param pos: position of the bomb
        :param border: border of the screen
        :param speed: speed for the bomb
        """
        self.pos = pos
        self.painter = Turtle()
        self.border = border
        self.speed = speed

    def set_bomb(self):
        """
        set bomb at the starting point
        """
        self.painter.speed(0)
        self.painter.pendown()
        self.painter.shape("bomb.gif")
        self.painter.penup()
        self.painter.goto(self.pos.x, self.pos.y)


    def update(self):
        """
        Making the bomb object fall down and when the bomb is off the screen
        random the position x to make it falling again.
        """
        self.pos.y = self.pos.y - self.speed
        if self.pos.y < self.border.bottom:
            self.pos.y = self.border.top
            self.pos.x = random.randint(self.border.left, self.border.right)

        self.painter.goto(self.pos.x, self.pos.y)


