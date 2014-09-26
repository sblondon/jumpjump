# -*- coding: utf-8 -*-

import pygame.image
import pygame.sprite

import consts


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x):
        super(Player, self).__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect().move(x, 150)
        self.mask = pygame.mask.from_surface(self.image)
        
        self.change_x = 0
        self.change_y = 0

        self.level = None

    def update(self):
        self._gravity_effect()
        self._move()

    def _move(self):
        self.rect.x += self.change_x

        block_hits = pygame.sprite.spritecollide(self, self.level.platform_sprites, False)
        for block in block_hits:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hits = pygame.sprite.spritecollide(self, self.level.platform_sprites, False)
        for block in block_hits:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

        if self.rect.left < 0 or self.rect.right > consts.WINDOW_SIZE[0]:
            self.change_x = 0

    def go_to_right(self):
        self.change_x = 1

    def go_to_left(self):
        self.change_x = -1

    def jump(self):
        if self._is_on_floor() or self._is_on_platform():
            self.change_y = -10

    def _is_on_floor(self):
        return self.rect.bottom >= consts.WINDOW_SIZE[1] 

    def _is_on_platform(self):
        self.rect.y += 2
        platform_hits = pygame.sprite.spritecollide(self, self.level.platform_sprites, False)
        self.rect.y -= 2
        return platform_hits

    def stop_go_to_left(self):
        if self.change_x < 0:
            self.change_x = 0

    def stop_go_to_right(self):
        if self.change_x > 0:
            self.change_x = 0

    def _gravity_effect(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.y >= consts.WINDOW_SIZE[1] - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = consts.WINDOW_SIZE[1] - self.rect.height


class Red(Player):
    def __init__(self):
        super(Red, self).__init__("gfx/person-red.png", x=50)

    def __unicode__(self):
        return u"Red player"


class Blue(Player):

    def __init__(self):
        super(Blue, self).__init__("gfx/person-blue.png", x=100)

    def __unicode__(self):
        return u"Blue player"
