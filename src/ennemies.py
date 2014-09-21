# -*- coding: utf-8 -*-

import pygame.image
import pygame.mask
import pygame.sprite

import consts


class Ennemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Ennemy, self).__init__()
        self.image = pygame.image.load("gfx/ennemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = [2, 2]
        self.position = self.image.get_rect().move(250, 150)

    def update(self):
        self.move()

    def move(self):
        self.position = self.position.move(self.speed)
        if self.position.left < 0 or self.position.right > consts.WINDOW_SIZE[0]:
            self.speed[0] *= -1
        if self.position.top < 0 or self.position.bottom > consts.WINDOW_SIZE[1]:
            self.speed[1] *= -1


    def touch(self, player):
        hitbox = self.position.inflate(-5, -5)
        return hitbox.colliderect(player.position)

