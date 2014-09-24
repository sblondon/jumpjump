# -*- coding: utf-8 -*-

import pygame.sprite

class Level(object):
    def __init__(self):
        self.platform_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.ennemy_sprites = pygame.sprite.Group()
        self.background = None

    def update(self):
        screen = pygame.display.get_surface()

        for sprite in self.player_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.ennemy_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.platform_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        self.player_sprites.update()
        self.player_sprites.draw(screen)

        self.ennemy_sprites.update()
        self.ennemy_sprites.draw(screen)

        self.platform_sprites.update()
        self.platform_sprites.draw(screen)
      
    def player_dies(self):
        for ennemy in self.ennemy_sprites:
            for player in self.player_sprites:
                if ennemy.touch(player):
                    print unicode(player) + u" lost 1 life"
                    return True
     
