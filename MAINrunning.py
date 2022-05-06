from runing import Game
from screen import Stage
from time import sleep
import json

list_score = []
# set the stage
stage = Stage(width=550, height=550)
stage.screen.clear()
stage.screen.bgpic("intro.gif")
player_num = int(stage.screen.textinput(title="Player", prompt="How many player? (Type only number)"))

oneround = Game(score=0, LIVE=3)

if player_num == 1:  # If there is one player in the game.
    oneround.oneround_setting(1)  # play one round
    # read score form data file.
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print("File not found")
    else:
        # report the player's score.
        stage.paint.clear()
        stage.paint.goto(0, 0)
        stage.paint.pendown()
        stage.screen.bgpic("winner.gif")
        stage.paint.write(f"Your score is {data['Player1']}", align="center", font=("arial", 30, "bold"))

else:  # If there are more than one players in the game.
    for i in range(player_num):
        if player_num-i >= 1:  # If there are still players who haven't played yet.
            oneround.oneround_setting(i+1)
            oneround.score = 0
            oneround.LIVE = 3
            if player_num-i != 1:  # if there have to start a round.
                stage.screen.clear()
                stage.screen.bgpic("count.gif")
                stage.count("3")
                sleep(0.8)
                stage.count("2")
                sleep(0.8)
                stage.count("1")
                sleep(0.8)
                stage.paint.clear()

            elif player_num-i == 1:  # if all players is already play.
                # read player's score from data file.
                try:
                    with open("data.json", "r") as data_file:
                        data = json.load(data_file)
                except FileNotFoundError:
                    print("File not found")
                else:
                    for x in range(len(data)):
                        # append all player's score in list to find the winner
                        list_score.append(data[f"Player{x + 1}"])
                    max_score = max(list_score)
                    winner_index = list_score.index(max_score)
                    if list_score.count(max_score) == 1:  # If there is only one highest score.
                        stage.paint.clear()
                        stage.paint.penup()
                        stage.paint.goto(0, 40)
                        stage.paint.pendown()
                        stage.paint.write(f"THE WINNER IS", align="center", font=("arial", 30, "bold"))
                        stage.paint.penup()
                        stage.paint.goto(0, -30)
                        stage.paint.pendown()
                        stage.screen.bgpic("winner.gif")
                        # report who the winner with winner player's score.
                        stage.paint.write(f"Player{winner_index+1}(SCORE: {list_score[winner_index]})",
                                          align="center", font=("arial", 30, "bold"))
                    elif list_score.count(max_score) > 1:  # if players are draw.
                        stage.paint.clear()
                        stage.paint.penup()
                        stage.paint.goto(0, 0)
                        stage.paint.pendown()
                        stage.screen.bgpic("winner.gif")
                        # report
                        stage.paint.write(f"That's Draw", align="center", font=("arial", 50, "bold"))


stage.screen.mainloop()
