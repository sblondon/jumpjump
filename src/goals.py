# -*- coding: utf-8 -*-
import random

import pygame.image
import pygame.sprite

import engine


class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y, level, teleport=False):
        super(Goal, self).__init__()
        self._IMAGES = {"blue": engine.image_path("goal-blue.png"), "red": engine.image_path("goal-red.png")}
        self._current_color = random.choice(self._IMAGES.keys())
        self.image = self._set_image()
        self.rect = self.image.get_rect().move(x, y)
        self._player_touch_done = 0
        self.player_touch_required = 3
        self._teleport = teleport

        self.level = level
        self._screen = pygame.display.get_surface()
        self._max_teleportable_x = self._screen.get_width() - self.rect.width

    def update(self):
        if (pygame.sprite.collide_rect(self, self.level.red_player) \
                and self._current_color == "red" \
                and not self.level.red_player.on_goal_previous_loop) or \
           (pygame.sprite.collide_rect(self, self.level.blue_player) \
                and self._current_color == "blue" \
                and not self.level.blue_player.on_goal_previous_loop):
           self._player_touch_done += 1
           self._current_color = "blue" if self._current_color == "red" else "red"
           self.image = self._set_image()
           if self._teleport:
                x = random.randint(0, self._max_teleportable_x)
                self.rect = self.image.get_rect().move(x, self.rect.y)
    
        if pygame.sprite.collide_rect(self, self.level.red_player):
           self.level.red_player.on_goal_previous_loop = True
        else:
           self.level.red_player.on_goal_previous_loop = False

        if pygame.sprite.collide_rect(self, self.level.blue_player):
           self.level.blue_player.on_goal_previous_loop = True
        else:
           self.level.blue_player.on_goal_previous_loop = False


    def _set_image(self):
        return pygame.image.load(self._IMAGES[self._current_color]).convert_alpha()

    def reached(self):
        return self._player_touch_done >= self.player_touch_required

