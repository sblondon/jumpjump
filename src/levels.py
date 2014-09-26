# -*- coding: utf-8 -*-

import pygame.sprite

import ennemies
import goals
import platforms
import players


class Level(object):
    def __init__(self):
        self.platform_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.ennemy_sprites = pygame.sprite.Group()
        self.goal_sprites = pygame.sprite.Group()
        self.background = None
        self.red_player = None
        self.blue_player = None
        self.goal = None

    def update(self):
        screen = pygame.display.get_surface()

        for sprite in self.player_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.ennemy_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.platform_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.goal_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        self.player_sprites.update()
        self.player_sprites.draw(screen)

        self.ennemy_sprites.update()
        self.ennemy_sprites.draw(screen)

        self.platform_sprites.update()
        self.platform_sprites.draw(screen)

        self.goal_sprites.update()
        self.goal_sprites.draw(screen)
      
    def players_die(self):
        return pygame.sprite.groupcollide(
                self.ennemy_sprites, self.player_sprites,
                False, False,
                collided=pygame.sprite.collide_mask)
    
    def players_win(self):
        return self.goal.reached()


    def create_ennemy(self):
        ennemy = ennemies.Ennemy()
        self.ennemy_sprites.add(ennemy)
        return ennemy
    
    def create_red_player(self):
        red = players.Red()
        red.level = self
        self.player_sprites.add(red)
        self.red_player = red
        return red

    def create_blue_player(self):
        blue = players.Blue()
        blue.level = self
        self.player_sprites.add(blue)
        self.blue_player = blue
        return blue

    def create_platform(self, x, y):
        platform = platforms.Platform()
        platform.rect.x = x
        platform.rect.y = y
        self.platform_sprites.add(platform)
        return platform
       
    def create_goal(self, x, y):
        goal = goals.Goal()
        goal.level = self
        goal.rect.x = x
        goal.rect.y = y
        self.goal = goal
        self.goal_sprites.add(goal)
        return goal

