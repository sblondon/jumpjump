import datetime

import pygame.sprite

import engine
import ennemies


class BasePlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, image_filename):
        super(BasePlatform, self).__init__()
        self.image = pygame.image.load(engine.image_path(image_filename)).convert_alpha()
        self.rect = self.image.get_rect().move(x, y)


class DefaultPlatform(BasePlatform):
    def __init__(self, x, y):
        super(DefaultPlatform, self).__init__(x, y, "default-platform.png")


class OctopusGeneratorPlatform(BasePlatform):
    def __init__(self, x, y, level):
        super(OctopusGeneratorPlatform, self).__init__(x, y, "octopus-platform.png")
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

