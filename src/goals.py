# -*- coding: utf-8 -*-

import pygame.image
import pygame.sprite


class Goal(pygame.sprite.Sprite):
    def __init__(self):
        super(Goal, self).__init__()
        self.image = pygame.image.load("gfx/goal-blue.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.level = None

    def update(self):
        collisions = pygame.sprite.groupcollide(self.level.goal_sprites, self.level.player_sprites, False, False)
        if collisions:
            print collisions, collisions.values()[0]
            if self.level.red_player in collisions.values()[0]:
                self.image = pygame.image.load("gfx/goal-red.png").convert_alpha()
            else:
                self.image = pygame.image.load("gfx/goal-blue.png").convert_alpha()


