# -*- coding: utf-8 -*-
import abc
import datetime
import math
import random

import pygame.display
import pygame.image
import pygame.mask
import pygame.sprite

import engine


class BaseKiller(pygame.sprite.Sprite):
    def touch_player(self, game):
        game.status = game.LOSE
        game.lives -= 1


class BaseFantom(BaseKiller):

    def __init__(self, x, y, speed, image):
        super(BaseFantom, self).__init__()
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


class SlowFantom(BaseFantom):
    def __init__(self, x, y):
        super(SlowFantom, self).__init__(x, y, [1, 1], engine.image_path("slow-fantom.png"))


class FastFantom(BaseFantom):
    def __init__(self, x, y):
        super(FastFantom, self).__init__(x, y, [2, 2], engine.image_path("fast-fantom.png"))


class Octopus(pygame.sprite.Sprite):

    def __init__(self, x, y, level):
        super(Octopus, self).__init__()
        self.image = pygame.image.load(engine.image_path("octopus.png")).convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.level = level
        self.target = random.choice((self.level.red_player, self.level.blue_player))

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
    IMAGE_QTY = 9

    def __init__(self, center_x, center_y):
        super(Ink, self).__init__()
        self.image_step = 0
        self.creation_datetime = datetime.datetime.now()
        self.image = self._set_image()
        x = center_x - self.image.get_width() / 2
        y = center_y - self.image.get_height() / 2
        self.rect = self.image.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self._screen = pygame.display.get_surface()

    def update(self):
        _seconds = 10 + 3 * self.image_step
        delay = datetime.timedelta(seconds=_seconds)
        if datetime.datetime.now() - self.creation_datetime > delay:
            if self.image_step < self.IMAGE_QTY - 1:
                self.image_step += 1
                self.image = self._set_image()
            else:
                self.kill()

    def _image_filename(self):
        return "ink-%d.png" % self.image_step

    def _set_image(self):
        return pygame.image.load(
                engine.image_path(self._image_filename())).convert_alpha()


class BaseBird(BaseKiller):
    X_OFFSET = 50
    X_SPEED = 3

    def __init__(self, y, to_right=True):
        super(BaseBird, self).__init__()
        self._screen = pygame.display.get_surface()

        self._to_right = to_right
        self._wings_up = True
        self.image = self._set_image()
        x_start = -self.X_OFFSET if to_right else self._screen.get_width() + self.X_OFFSET
        self.rect = self.image.get_rect().move(x_start, y)
        self.mask = pygame.mask.from_surface(self.image)
        self._x_speed = self.X_SPEED if to_right else -self.X_SPEED
        self._last_flap = datetime.datetime.now()

    @abc.abstractmethod
    def update(self):
        y = 5 * math.cos(self.rect.x * 2)
        speed = [self._x_speed, y]
        self.rect = self.rect.move(speed)
        self.flap()

    def flap(self):
        delay = datetime.timedelta(milliseconds=300)
        if datetime.datetime.now() - self._last_flap > delay:
            self._wings_up = not self._wings_up
            self._last_flap = datetime.datetime.now()
            self.image = self._set_image()

    def _set_image(self):
        image = "bird-0.png" if self._wings_up else "bird-1.png"
        surface = pygame.image.load(
                engine.image_path(image)).convert_alpha()
        return surface if self._to_right else pygame.transform.flip(surface, True, False)


class LeftBird(BaseBird):
    def __init__(self, y):
        super(LeftBird, self).__init__(y, True)

    def update(self):
        super(LeftBird, self).update()
        if self.rect.left > self._screen.get_width():
            self.kill()


class RightBird(BaseBird):
    def __init__(self, y):
        super(RightBird, self).__init__(y, False)

    def update(self):
        super(RightBird, self).update()
        if self.rect.right < 0:
            self.kill()

