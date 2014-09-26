# -*- coding: utf-8 -*-

import pygame.image
import pygame.sprite


class Goal(pygame.sprite.Sprite):
    def __init__(self):
        super(Goal, self).__init__()
        self._IMAGES = {"blue": "gfx/goal-blue.png", "red": "gfx/goal-red.png"}
        self._current_color = "blue"
        self._reset_image()
        self.rect = self.image.get_rect()
        self._player_touch_done = 0
        self._player_touch_required = 3

        self.level = None


    def update(self):
        collisions = pygame.sprite.groupcollide(self.level.goal_sprites, self.level.player_sprites, False, False)
        if collisions:
            if self.level.red_player in collisions.values()[0] and self._current_color == "red":
                self._player_touch_done += 1
                self._current_color = "blue"
                self._reset_image()
            elif self.level.blue_player in collisions.values()[0] and self._current_color == "blue":
                self._player_touch_done += 1
                self._current_color = "red"
                self._reset_image()

    def _reset_image(self):
        self.image = pygame.image.load(self._IMAGES[self._current_color]).convert_alpha()


    def reached(self):
        return self._player_touch_done >= self._player_touch_required

