# -*- coding: utf-8 -*-

import pygame.display
import pygame.image
import pygame.mask
import pygame.sprite

import engine


class BouncingEnnemy(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, image):
        super(BouncingEnnemy, self).__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self._speed = speed

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


class SlowBouncingEnnemy(BouncingEnnemy):
    def __init__(self, x, y):
        super(SlowBouncingEnnemy, self).__init__(x, y, [1, 1], engine.image_path("slow-bouncing.png"))


class FastBouncingEnnemy(BouncingEnnemy):
    def __init__(self, x, y):
        super(FastBouncingEnnemy, self).__init__(x, y, [2, 2], engine.image_path("fast-bouncing.png"))

