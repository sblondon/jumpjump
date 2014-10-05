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
        self.rect = self.rect.move(self._speed)
        if self.rect.left < 0 or self.rect.right > self._screen.get_width():
            self._speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > self._screen.get_height():
            self._speed[1] *= -1

    def touch_player(self, game):
        game.status = game.LOSE
        game.lives -= 1
        


class SlowBouncingEnnemy(BouncingEnnemy):
    def __init__(self, x, y):
        super(SlowBouncingEnnemy, self).__init__(x, y, [1, 1], engine.image_path("slow-bouncing.png"))


class FastBouncingEnnemy(BouncingEnnemy):
    def __init__(self, x, y):
        super(FastBouncingEnnemy, self).__init__(x, y, [2, 2], engine.image_path("fast-bouncing.png"))


class Octopus(pygame.sprite.Sprite):

    def __init__(self, x, y, target, level):
        super(Octopus, self).__init__()
        self.image = pygame.image.load(engine.image_path("octopus.png")).convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.target = target
        self.level = level

        self._screen = pygame.display.get_surface()

    def update(self):
        MOVE = 1
        if self.rect.x < self.target.rect.x and self.rect.right < self._screen.get_width():
            self.rect.x += MOVE
        elif self.rect.x > self.target.rect.x:
            self.rect.x -= MOVE

        if self.rect.y < self.target.rect.y and not self._is_on_floor():
            self.rect.y += MOVE
        elif self.rect.y > self.target.rect.y:
            self.rect.y -= MOVE

    def _is_on_floor(self):
        return self.rect.bottom >= self._screen.get_height()

    def touch_player(self, game):
        if pygame.sprite.collide_mask(self, self.target):
            self.create_ink()
            self.kill()

    def create_ink(self):
        ink = Ink(self.rect.x, self.rect.y)
        self.level.ink_sprites.add(ink)
        self.level.all_sprites.add(ink)


class Ink(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Ink, self).__init__()
        self.image = pygame.image.load(engine.image_path("ink.png")).convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self._screen = pygame.display.get_surface()

