# -*- coding: utf-8 -*-

import engine

from core import Level


class Level0(Level):
    def __init__(self, game):
        super(Level0, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_default_platform(350, 50)
        self.create_default_platform(350, 100)
        self.create_goal(400, 400)
        self.finalize_level()

    def create_ennemies(self):
        self.create_slow_bouncing_ennemy(250, 150)


class Level1(Level):
    def __init__(self, game):
        super(Level1, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_default_platform(300, 350)
        self.create_teleportable_goal(500, 400)
        self.finalize_level()

    def create_ennemies(self):
        self.create_fast_bouncing_ennemy(50, 50)


class Level2(Level):
    def __init__(self, game):
        super(Level2, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_default_platform(200, 420)
        self.create_goal(300, 350)
        self.finalize_level()

    def create_ennemies(self):
        self.create_slow_bouncing_ennemy(250, 50)
        self.create_slow_bouncing_ennemy(450, 150)


class Level3(Level):
    def __init__(self, game):
        super(Level3, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_default_platform(250, 420)
        self.create_goal(250, 300)
        self.finalize_level()

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_slow_bouncing_ennemy(250, 50)
        self.create_slow_bouncing_ennemy(450, 150)


class Level4(Level):
    def __init__(self, game):
        super(Level4, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_default_platform(250, 420)
        self.create_goal(250, 300)
        self.finalize_level()

    def create_ennemies(self):
        self.create_octopus(450, 50)
        self.create_left_bird(250)
        self.create_right_bird(320)

