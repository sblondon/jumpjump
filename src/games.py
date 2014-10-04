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

