# -*- coding: utf-8 -*-
import random

import pygame.image
import pygame.sprite

import engine


class Goal(pygame.sprite.Sprite):
    def __init__(self):
        super(Goal, self).__init__()
        self._IMAGES = {"blue": engine.image_path("goal-blue.png"), "red": engine.image_path("goal-red.png")}
        self._current_color = random.choice(self._IMAGES.keys())
        self.image = self._set_image()
        self.rect = self.image.get_rect()
        self._player_touch_done = 0
        self._player_touch_required = 3

        self.level = None

    def update(self):
       if (pygame.sprite.collide_rect(self, self.level.red_player) and self._current_color == "red") or \
          (pygame.sprite.collide_rect(self, self.level.blue_player) and self._current_color == "blue"):
           self._player_touch_done += 1
           self._current_color = "blue" if self._current_color == "red" else "red"
           self.image = self._set_image()

    def _set_image(self):
        return pygame.image.load(self._IMAGES[self._current_color]).convert_alpha()

    def reached(self):
        return self._player_touch_done >= self._player_touch_required

