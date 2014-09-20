# -*- coding: utf-8 -*-

import pygame

import consts


class Ennemy(object):

    def __init__(self):
        self.image = pygame.image.load("gfx/ennemy.png").convert_alpha()
        self.speed = [2, 2]
        self.position = self.get_rect().move(250, 150)

    def get_rect(self):
        return self.image.get_rect()

    def move(self):
        self.position = self.position.move(self.speed)
        if self.position.left < 0 or self.position.right > consts.WINDOW_SIZE[0]:
            self.speed[0] *= -1
        if self.position.top < 0 or self.position.bottom > consts.WINDOW_SIZE[1]:
            self.speed[1] *= -1

    def should_move(self):
        return True

    def touch(self, player):
        hitbox = self.position.inflate(-5, -5)
        return hitbox.colliderect(player.position)
