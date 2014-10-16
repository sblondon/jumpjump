# -*- coding: utf-8 -*-
import os
import random

import pygame.display

import engine

from core import BaseLevel


class Level0(BaseLevel):
    def __init__(self, game):
        super(Level0, self).__init__(game, engine.background_path("wall.png"))
        self.create_ennemies()
        self.create_default_platform(350, 50)
        self.create_default_platform(350, 100)
        self.create_goal(400, 400)
        self.finalize_level()

    def create_ennemies(self):
        self.create_slow_fantom(250, 150)


class Level1(BaseLevel):
    def __init__(self, game):
        super(Level1, self).__init__(game, engine.background_path("bridge.png"))
        self.create_ennemies()
        self.create_default_platform(300, 350)
        self.create_teleportable_goal(500, 400)
        self.finalize_level()

    def create_ennemies(self):
        self.create_fast_fantom(50, 50)


class Level2(BaseLevel):
    def __init__(self, game):
        super(Level2, self).__init__(game, engine.background_path("desert-1.png"))
        self.create_ennemies()
        self.create_default_platform(200, 420)
        self.create_goal(300, 350)
        self.finalize_level()

    def create_ennemies(self):
        self.create_slow_fantom(250, 50)
        self.create_slow_fantom(450, 150)


class Level3(BaseLevel):
    def __init__(self, game):
        super(Level3, self).__init__(game, engine.background_path("desert-2.png"))
        self.create_ennemies()
        self.create_default_platform(250, 420)
        self.create_goal(250, 300)
        self.finalize_level()

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_slow_fantom(250, 50)
        self.create_slow_fantom(450, 150)


class Level4(BaseLevel):
    def __init__(self, game):
        super(Level4, self).__init__(game, engine.background_path("wall.png"))
        self.create_ennemies()
        self.create_octopus_platform(250, 420)
        self.create_goal(250, 300)
        self.finalize_level()

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_left_bird(250)
        self.create_right_bird(320)


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
        super(RandomLevel, self).__init__(game, engine.background_path(background_filename))
        self._game = game
        self._screen = pygame.display.get_surface()
        self.create_platforms()
        self.create_ennemies()
        self.finalize_level()

    def create_platforms(self):
        self.create_octopus_platform(250, 420)
        goal = self.create_goal(250, 300)
        goal.player_touch_required = self._game.won_levels

    def create_ennemies(self):
        for enn, qty in self._game.random_ennemies.items():
            for i in range(qty):
                self.create_ennemy(enn)

        enn = random.choice( self._game.random_ennemies.keys() )
        self.create_ennemy(enn)
        self._game.random_ennemies[enn] += 1

    def create_ennemy(self, enn):
       if enn == self._game.SLOW_FANTOM:
           x = random.randint(0, self._screen.get_width() - 50)
           self.create_slow_fantom(x, 50)
       elif enn == self._game.FAST_FANTOM:
           x = random.randint(0, self._screen.get_width() - 50)
           self.create_fast_fantom(x, 50)
       elif enn == self._game.OCTOPUS:
           x = random.randint(0, self._screen.get_width() - 50)
           self.create_octopus(x, 150)
       elif enn == self._game.LEFT_BIRD:
           y = random.randint(0, self._screen.get_height() - 100)
           self.create_left_bird(y)
       elif enn == self._game.RIGHT_BIRD:
           y = random.randint(0, self._screen.get_height() - 100)
           self.create_right_bird(y)

