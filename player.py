import copy
from turtle import Turtle
from vector import Vector
from border import Border


class Player:
    def __init__(self, pos=Vector(0, 0), shape="square", border=Border(width=550, height=550)):
        """

        :param pos: position of player
        :type pos: Vector object
        :param shape: shape of player
        :type shape: str
        :param border: border of the stage
        :type border: Border object
        """
        self.pos = pos
        self.shape = shape
        self.painter = Turtle()
        self.border = border

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, val):
        if not isinstance(val, Vector):
            raise TypeError('position must be a Vector object')
        self.__pos = copy.copy(val)

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, string):
        if not isinstance(string, str):
            raise TypeError("shape must be string")
        self.__shape = string

    def set_player(self):
        """
        Set the player in the position.
        :return:
        """
        self.painter.speed(0)
        self.painter.pendown()
        self.painter.shape(self.shape)
        self.painter.penup()
        self.painter.goto(self.pos.x, self.pos.y)

    def go_left(self):
        """
        Move the player to the left without going out of the border.
        """
        self.pos.x -= 10
        self.painter.goto(self.pos.x, self.pos.y)
        if self.pos.x <= self.border.left:
            self.pos.x = self.border.left
        self.painter.shape("pig_2.gif")

    def go_right(self):
        """
        Move the player to the right without going out of the border.
        """
        self.pos.x += 10
        self.painter.goto(self.pos.x, self.pos.y)
        if self.pos.x > self.border.right:
            self.pos.x = self.border.right
        self.painter.shape("pig.gif")





