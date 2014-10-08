# -*- coding: utf-8 -*-
import datetime

import pygame.sprite

import engine
import ennemies


class Platform(pygame.sprite.Sprite):
    def __init__(self, image_filename):
        super(Platform, self).__init__()
        self.image = pygame.image.load(engine.image_path(image_filename)).convert_alpha()
        self.rect = self.image.get_rect()


class DefaultPlatform(Platform):
    def __init__(self):
        super(DefaultPlatform, self).__init__("default-platform.png")


class OctopusGeneratorPlatform(Platform):
    def __init__(self, level):
        super(OctopusGeneratorPlatform, self).__init__("octopus-platform.png")
        self.last_generation = datetime.datetime.now()
        self.level = level

    def update(self):
        delay = datetime.timedelta(seconds=12)
        if datetime.datetime.now() - self.last_generation > delay:
            self.create_octopus()
            self.last_generation = datetime.datetime.now()

    def create_octopus(self):
        octopus = ennemies.Octopus(self.rect.x, self.rect.y, self.level)
        self.level.ennemy_sprites.add(octopus)
        self.level.all_sprites.add(octopus)

