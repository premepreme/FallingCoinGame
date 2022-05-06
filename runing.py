from screen import Stage
from vector import Vector
from player import Player
from coin import Coin
from bomb import Bomb
from time import sleep
import json
import time
import random

TIME_STEP = 0.01


class Game:
    def __init__(self, score=0, LIVE=3):
        """
        :param score: score that player get
        :type score: int
        :param LIVE: live that player have.
        :type LIVE: int
        """
        self.score = score
        self.LIVE = LIVE
        stage = Stage(width=550, height=550)
        self.stage = stage


    def collect(self, distance):
        """
        Checking if players collect coins or not.if already collect +10 to player's score
        and the new coin will drop on the top by random position.
        :param distance: distance shortest between coin and player.
        :type distance: int
        """
        if self.stage.coin.painter.distance(self.stage.player.painter) < distance:
            # if player can collect coin a new coin will drop on the top by random position.
            self.stage.coin.pos.x = random.randint(self.stage.border.left, self.stage.border.right)
            self.stage.coin.pos.y = self.stage.border.top
            self.stage.coin.painter.goto(self.stage.coin.pos.x, self.stage.coin.pos.y)
            self.score += 10  # get +10 in score
        self.stage.paint.clear()
        font = ("arial", 20, "bold")
        self.stage.paint.write(f"SCORE: {self.score}  LIVE: {self.LIVE}", align="center", font=font)

    def off_screen(self):
        """
        if the coin is out off border mean that player can't collect the coin.Then the player's live will -1
        and the new coin will drop on the top by random position.
        """
        if self.stage.coin.pos.y < self.stage.border.bottom:
            self.LIVE -= 1
            self.stage.coin.pos.y = self.stage.border.top
            self.stage.coin.pos.x = random.randint(self.stage.border.left, self.stage.border.right)
            self.stage.coin.painter.goto(self.stage.coin.pos.x, self.stage.coin.pos.y)
        self.stage.paint.clear()
        font = ("arial", 20, "bold")
        self.stage.paint.write(f"SCORE: {self.score}  LIVE: {self.LIVE}", align="center", font=font)

    def collect_bomb(self,distance):
        """
        Checking if players collect bomb or not.if the player collect it will -10 to player's score
        and the new bomb will continuous drop on the top by random position.
        :param distance: distance shortest between bomb and player.
        :type distance: int
        """
        if self.stage.bomb.painter.distance(self.stage.player.painter) < distance:
            self.stage.bomb.pos.x = random.randint(self.stage.border.left, self.stage.border.right)
            self.stage.bomb.pos.y = self.stage.border.top
            self.stage.bomb.pos.x = random.randint(self.stage.border.left, self.stage.border.right)
            self.stage.bomb.painter.goto(self.stage.bomb.pos.x, self.stage.bomb.pos.y)
            self.score -= 10
        self.stage.paint.clear()
        font = ("arial", 20, "bold")
        self.stage.paint.write(f"SCORE: {self.score}  LIVE: {self.LIVE}", align="center", font=font)

    def oneround_setting(self, num):
        """
        Setting all object and calling all function we need in one round.
        :param num: number of player in case that the game has more than 1 player.
        :type num: int
        """
        # set the stage
        self.stage.set_stage()
        self.stage.screen.tracer(0)
        self.stage.set_score(self.score, self.LIVE)

        self.stage.screen.register_shape("pig.gif")
        self.stage.screen.register_shape("pig_2.gif")
        self.stage.screen.register_shape("bomb.gif")
        self.stage.screen.register_shape("coin.gif")

        # set player position, shape and border
        player = Player(pos=Vector(0, -230), shape="pig.gif", border=self.stage.border)
        self.stage.player = player
        self.stage.player.set_player()


        # set coin position by random x
        coin = Coin(pos=Vector(random.randint(self.stage.border.left, self.stage.border.right), self.stage.border.top))
        self.stage.coin = coin
        self.stage.coin.set_coin()

        # set bomb position by random
        bomb = Bomb(pos=Vector(random.randint(self.stage.border.left, self.stage.border.right), self.stage.border.top))
        self.stage.bomb = bomb
        self.stage.bomb.set_bomb()

        self.stage.screen.listen()
        self.stage.screen.onkeypress(player.go_left, "Left")
        self.stage.screen.onkeypress(player.go_right, "Right")

        while True:
            if self.LIVE > 0:  # if player's live more than 0 mean the the game is continuous.
                self.collect(30)
                self.collect_bomb(20)
                self.off_screen()
                timestamp = time.time()
                self.stage.update()
                time.sleep(max(0, TIME_STEP - (time.time() - timestamp)))

            if self.LIVE == 0:   # if player's = 0 mean the the game is over.
                # then update the player's score to data file.
                player_data = {f"Player{num}": self.score}
                try:
                    with open("data.json", "r") as data_file:
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(player_data, data_file, indent=4)
                else:
                    data.update(player_data)
                    with open("data.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                sleep(0.5)
                self.stage.screen.clear()
                self.stage.game_over()  # report game over
                sleep(2)
                self.stage.screen.clear()
                break  # end
















