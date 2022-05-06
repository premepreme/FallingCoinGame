from turtle import Turtle, Screen
from coin import Coin
from bomb import Bomb
from player import Player
from border import Border


class Stage:

    def __init__(self, width=0, height=0, coin=Coin(), bomb=Bomb(), player=Player()):
        """
        :param width: width of the stage
        :type width: int
        :param height: height of the stage
        :type height: int
        :param coin: coin object that drop from the top of the stage
        :type coin: Coin object
        :param bomb: bomb object that drop from the top of the stage
        :type bomb: Bomb object
        :param player: player object the move left and right to collect the coin
        :type player: Player object
        """
        self.screen = Screen()
        self.paint = Turtle()
        self.width = width
        self.height = height
        self.coin = coin
        self.bomb = bomb
        self.player = player
        self.border = Border(width=width, height=height)


    @property
    def coin(self):
        """
        Create a property, which can be directly accessed.
        :return: the color's value
        """
        return self.__coin

    @coin.setter
    def coin(self, val):
        """
        The color property must be a  string value,if not raise TypeError.
        then set color to a new string value.
        :param val: string value
        """
        self.__coin = val

    @property
    def bomb(self):
        """
        Create a property, which can be directly accessed.
        :return: the color's value
        """
        return self.__bomb

    @bomb.setter
    def bomb(self, val):
        """
        The color property must be a  string value,if not raise TypeError.
        then set color to a new string value.
        :param val: string value
        """
        self.__bomb = val

    def set_stage(self):
        """
        setting stage add a picture og background
        """
        self.screen.setup(width=self.width, height=self.height, startx=0, starty=0)
        self.screen.bgpic("background.gif")


    def set_score(self, score, live):
        """
        report score to the stage
        :param score: score that player get
        :type score:int
        :param live: live that the player have left
        :type live:int
        :return:
        """
        self.paint.hideturtle()
        self.paint.speed(0)
        self.paint.color("black")
        self.paint.penup()
        self.paint.goto(0, self.border.top-50)
        font = ("arial", 20, "bold")
        self.paint.write(f"SCORE: {score}  LIVE: {live}", align="center", font=font)

    def game_over(self):
        """
        report that the game is over by show the word "Game Over" on the stage
        """
        self.paint.clear()
        font = ("arial", 50, "bold")
        self.paint.clear()
        self.screen.bgpic("gameover.gif")
        self.paint.penup()
        self.paint.goto(0, 0)
        self.paint.pendown()
        self.paint.write(f"GAME OVER", align="center", font=font)


    def count(self, x):
        """
        countdown to let player know that the round will start soon
        :param x: number that we want function to count
        :type x: str
        """
        self.paint.clear()
        font1 = ("arial", 20, "bold")
        font2 = ("arial", 40, "bold")
        self.paint.clear()
        self.paint.penup()
        self.paint.goto(0, 50)
        self.paint.pendown()
        self.paint.write(f"New Round start in", align="center", font=font1)
        self.paint.penup()
        self.paint.goto(0, -20)
        self.paint.pendown()
        self.paint.write(f"{x}", align="center", font=font2)


    def update(self):
        """
        update the object coin and bomb on the stage
        """
        self.__coin.update()
        self.__bomb.update()
        self.screen.update()







