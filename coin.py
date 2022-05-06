from vector import Vector
from turtle import Turtle
import copy


class Coin:
    def __init__(self, pos=Vector(0, 0),speed=3):
        """
        A coin object initialized with three properties
        :param pos: position of the coin
        :param speed: speed that the ball drop
        """
        self.pos = pos
        self.painter = Turtle()
        self.speed = speed

    @property
    def pos(self):
        """
        Create a property, which can be directly accessed.
        :return: the position's value
        """
        return self.__pos

    @pos.setter
    def pos(self, val):
        """
        The position property must be a Vector object,if not raise TypeError.
        then set corner to a new value.
        :param val: Vector object
        """
        if not isinstance(val, Vector):
            raise TypeError('pos must be a Vector object')
        self.__pos = copy.copy(val)

    @property
    def speed(self):
        """
        Create a property, which can be directly accessed.
        :return: the speed's value
        """
        return self.__speed

    @speed.setter
    def speed(self, val):
        """
        The speed property must be a integer,if not raise TypeError.
        then set velocity to a new value.
        :param val: Vector object
        """
        if not isinstance(val, int):
            raise TypeError('speed must be a int')
        self.__speed = copy.copy(val)

    def set_coin(self):
        """
        set coin at the starting point
        """
        self.painter.speed(0)
        self.painter.pendown()
        self.painter.shape("coin.gif")
        self.painter.penup()
        self.painter.goto(self.pos.x, self.pos.y)

    def update(self):
        """
        making the coin object fall down
        """
        self.pos.y = self.pos.y - self.speed
        self.painter.goto(self.pos.x, self.pos.y)












