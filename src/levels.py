# -*- coding: utf-8 -*-

import pygame.sprite

class Level(object):
    def __init__(self):
        self.platform_sprites = pygame.sprite.Group()
        self.movable_sprites = pygame.sprite.Group()
        self.background = None

    def update(self):
        screen = pygame.display.get_surface()

        for sprite in self.movable_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.platform_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        self.movable_sprites.update()
        self.movable_sprites.draw(screen)

        self.platform_sprites.update()
        self.platform_sprites.draw(screen)
       
