# -*- coding: utf-8 -*-

import pygame.sprite

import engine


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.image = pygame.image.load(engine.image_path("platform.png")).convert_alpha()
        self.rect = self.image.get_rect()

