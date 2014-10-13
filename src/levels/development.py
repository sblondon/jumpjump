# -*- coding: utf-8 -*-

import engine

from core import BaseLevel
from progress import RandomLevel


class TestLevel(RandomLevel):
    pass
#    def __init__(self, game):
#        super(TestLevel, self).__init__(game, engine.image_path("background.png"))
#        self.create_ennemies()
#        self.create_octopus_platform(350, 100)
#        self.create_teleportable_goal(400, 400)
#        self.finalize_level()
#
#    def create_ennemies(self):
#        self.create_left_bird(50)
#        self.create_right_bird(100)
#
