# -*- coding: utf-8 -*-

import engine

from core import Level


class TestLevel(Level):
    def __init__(self, game):
        super(TestLevel, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_platform(350, 50)
        self.create_platform(350, 100)
        self.create_goal(400, 400)
        self.finalize_level()

    def create_ennemies(self):
        self.create_octopus(250, 150)

