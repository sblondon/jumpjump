# -*- coding: utf-8 -*-

class Game(object):
    QUIT = "Quit"
    WIN = "Win"
    LOSE = "Lose"

    def __init__(self):
        self.reset()

    def reset(self):
        self.won_levels = 0
        self.lives = 3
        self.play_again = True
        self.status = None
        self.random_ennemies = {
                "slow": 0,
                "fast": 0,
                "octopus": 1,
                "left": 1,
                "right": 0,
                }

