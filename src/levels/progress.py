import os
import random

import pygame.display

import engine
from . import core
from . import platformsbuilder


class Level0(core.BaseLevel):
    BACKGROUND_PATH = engine.background_path("wall.png")

    def create_ennemies(self):
        self.create_slow_fantom(250, 150)

    def create_platforms(self):
        platformsbuilder.platform0_builder(self)


class Level1(core.BaseLevel):
    BACKGROUND_PATH = engine.background_path("bridge.png")

    def create_ennemies(self):
        self.create_fast_fantom(50, 50)

    def create_platforms(self):
        platformsbuilder.platform1_builder(self)


class Level2(core.BaseLevel):
    BACKGROUND_PATH = engine.background_path("desert-1.png")

    def create_ennemies(self):
        self.create_slow_fantom(250, 50)
        self.create_slow_fantom(450, 150)

    def create_platforms(self):
        platformsbuilder.platform2_builder(self)


class Level3(core.BaseLevel):
    BACKGROUND_PATH = engine.background_path("desert-2.png")

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_slow_fantom(250, 50)
        self.create_slow_fantom(450, 150)

    def create_platforms(self):
        platformsbuilder.platform3_builder(self)


class Level4(core.BaseLevel):
    BACKGROUND_PATH = engine.background_path("wall.png")

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_left_bird(250)
        self.create_right_bird(320)

    def create_platforms(self):
        platformsbuilder.platform4_builder(self)



LEVELS = {0: Level0,
        1: Level1,
        2: Level2,
        3: Level3,
        4: Level4,
        }



class RandomLevel(core.BaseLevel):
    def __init__(self, game):
        backgrounds = os.listdir(engine.background_dir())
        background_filename = random.choice(backgrounds)
        self.BACKGROUND_PATH = engine.background_path(background_filename)
        super(RandomLevel, self).__init__(game)

    def create_platforms(self):
        platformsbuilder.random_builder(self)

    def create_ennemies(self):
        for ennemy_id, qty in self.game.random_ennemies.items():
            for i in range(qty):
                self._create_ennemy(ennemy_id)

        ennemy_id = random.choice(tuple(self.game.random_ennemies.keys()))
        self._create_ennemy(ennemy_id)
        self.game.random_ennemies[ennemy_id] += 1

    def _create_ennemy(self, ennemy_id):
        ennemy_creator = {
                self.game.SLOW_FANTOM: self._create_slow_fantom,
                self.game.FAST_FANTOM: self._create_fast_fantom,
                self.game.OCTOPUS: self._create_octopus,
                self.game.LEFT_BIRD: self._create_left_bird,
                self.game.RIGHT_BIRD: self._create_right_bird,

                }
        ennemy_creator[ennemy_id]()

    def _create_slow_fantom(self):
        x = random.randint(0, self.screen.get_width() - 50)
        y = random.randint(0, self.screen.get_height() - 200)
        self.create_slow_fantom(x, y)

    def _create_fast_fantom(self):
        x = random.randint(0, self.screen.get_width() - 50)
        y = random.randint(0, self.screen.get_height() - 150)
        self.create_fast_fantom(x, y)

    def _create_octopus(self):
        x = random.randint(0, self.screen.get_width() - 50)
        y = random.randint(125, 375)
        self.create_octopus(x, y)

    def _create_left_bird(self):
        y = random.randint(0, self.screen.get_height() - 100)
        self.create_left_bird(y)

    def _create_right_bird(self):
        y = random.randint(0, self.screen.get_height() - 100)
        self.create_right_bird(y)

