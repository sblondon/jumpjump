# -*- coding: utf-8 -*-
import os
import random

import pygame.display

import engine

from core import BaseLevel
import platformsbuilder

class Level0(BaseLevel):
    BACKGROUND_PATH = engine.background_path("wall.png")

    def create_ennemies(self):
        self.create_slow_fantom(250, 150)

    def create_platforms(self):
        platformsbuilder.level0_builder(self)


class Level1(BaseLevel):
    BACKGROUND_PATH = engine.background_path("bridge.png")

    def create_ennemies(self):
        self.create_fast_fantom(50, 50)

    def create_platforms(self):
        platformsbuilder.level1_builder(self)


class Level2(BaseLevel):
    BACKGROUND_PATH = engine.background_path("desert-1.png")

    def create_ennemies(self):
        self.create_slow_fantom(250, 50)
        self.create_slow_fantom(450, 150)

    def create_platforms(self):
        platformsbuilder.level2_builder(self)


class Level3(BaseLevel):
    BACKGROUND_PATH = engine.background_path("desert-2.png")

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_slow_fantom(250, 50)
        self.create_slow_fantom(450, 150)

    def create_platforms(self):
        platformsbuilder.level3_builder(self)


class Level4(BaseLevel):
    BACKGROUND_PATH = engine.background_path("wall.png")

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_left_bird(250)
        self.create_right_bird(320)

    def create_platforms(self):
        platformsbuilder.level4_builder(self)



LVLS = {0: Level0,
        1: Level1,
        2: Level2,
        3: Level3,
        4: Level4,
        }



class RandomLevel(BaseLevel):
    def __init__(self, game):
        backgrounds = os.listdir(engine.background_dir())
        background_filename = random.choice(backgrounds)
        self.BACKGROUND_PATH = engine.background_path(background_filename)
        super(RandomLevel, self).__init__(game)

    def create_platforms(self):
        platformsbuilder.random_builder(self)

    def create_ennemies(self):
        for enn, qty in self.game.random_ennemies.items():
            for i in range(qty):
                self.create_ennemy(enn)

        enn = random.choice( self.game.random_ennemies.keys() )
        self.create_ennemy(enn)
        self.game.random_ennemies[enn] += 1

    def create_ennemy(self, enn):
       if enn == self.game.SLOW_FANTOM:
           x = random.randint(0, self.screen.get_width() - 50)
           self.create_slow_fantom(x, 50)
       elif enn == self.game.FAST_FANTOM:
           x = random.randint(0, self.screen.get_width() - 50)
           self.create_fast_fantom(x, 50)
       elif enn == self.game.OCTOPUS:
           x = random.randint(0, self.screen.get_width() - 50)
           self.create_octopus(x, 150)
       elif enn == self.game.LEFT_BIRD:
           y = random.randint(0, self.screen.get_height() - 100)
           self.create_left_bird(y)
       elif enn == self.game.RIGHT_BIRD:
           y = random.randint(0, self.screen.get_height() - 100)
           self.create_right_bird(y)

