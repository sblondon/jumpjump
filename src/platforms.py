# -*- coding: utf-8 -*-

import pygame.sprite


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.image = pygame.image.load("gfx/platform.png").convert_alpha()
        self.rect = self.image.get_rect()

