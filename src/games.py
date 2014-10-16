# -*- coding: utf-8 -*-

class Game(object):
    QUIT = "Quit"
    WIN = "Win"
    LOSE = "Lose"

    SLOW_FANTOM = "slow"
    FAST_FANTOM = "fast"
    OCTOPUS = "octopus"
    LEFT_BIRD = "left"
    RIGHT_BIRD = "right"

    def __init__(self):
        self.reset()

    def reset(self):
        self.won_levels = 0
        self.lives = 3
        self.play_again = True
        self.status = None
        self.random_ennemies = {
                self.SLOW_FANTOM: 0,
                self.FAST_FANTOM: 0,
                self.OCTOPUS: 1,
                self.LEFT_BIRD: 1,
                self.RIGHT_BIRD : 0,
                }

