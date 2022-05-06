class Border:
    def __init__(self, width, height):
        """
        A Border object initialized with a width, and a height.
        :param width: width of the screen
        :param height: height of the screen
        """
        self.width = width
        self.height = height

    @property
    def left(self):
        """
        The left property gives the x-coordinate of the border's left side
        """
        return -self.width/2+10

    @property
    def right(self):
        """
        The right property gives the x-coordinate of the border's right side.
        """
        return self.width/2-10

    @property
    def bottom(self):
        """
        The bottom property gives the y-coordinate of the border's bottom.
        """
        return - self.height/2-10

    @property
    def top(self):
        """
        The top property gives the y-coordinate of the border's top side.
        """
        return self.height/2-10

    @property
    def width(self):
        """
        create a property, which can be directly accessed.
        :return: the width's value
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        The width property must be numbers, if not it will raise TypeError.
        and width property must greater than zero, if not it will raise ValueError
        Then set width to a new value.
        :param val: int , float
        """
        if not isinstance(val, (int, float)):
            raise TypeError('width must be a number')
        if val <= 0:
            raise ValueError('width must be greater than zero')
        self.__width = val

    @property
    def height(self):
        """
        create a property, which can be directly accessed.
        :return: the height's value
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        The height property must be numbers, if not it will raise TypeError.
        and height property must greater than zero, if not it will raise ValueError
        Then set height to a new value.
        :param val: int , float
        """
        if not isinstance(val, (int, float)):
            raise TypeError('height must be a number')
        if val <= 0:
            raise ValueError('height must be greater than zero')
        self.__height = val
