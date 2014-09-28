# -*- coding: utf-8 -*-

import pygame.display
import pygame.image
import pygame.mask
import pygame.sprite


class Ennemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Ennemy, self).__init__()
        self.image = pygame.image.load("gfx/ennemy.png").convert_alpha()
        self.rect = self.image.get_rect().move(250, 150)
        self.mask = pygame.mask.from_surface(self.image)
        self._speed = [2, 2]

        self._screen = pygame.display.get_surface()

    def update(self):
        self._move()

    def _move(self):
        self.rect = self.rect.move(self._speed)
        if self.rect.left < 0 or self.rect.right > self._screen.get_width():
            self._speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > self._screen.get_height():
            self._speed[1] *= -1

    def touch(self, player):
        hitbox = self.rect.inflate(-5, -5)
        if hitbox.colliderect(player.rect):
            return pygame.sprite.collide_mask(self, player)

