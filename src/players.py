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
        self.speed = [0, 0]
        self.move_requested = {"up": False, "left": False, "right": False}
        
        self.change_x = 0
        self.change_y = 0


    def update(self):
        self.gravity_effect()
        self.move()

    def move(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def move_enable(self, key):
        if key == "left":
            self.change_x = -1
        elif key == "right":
            self.change_x = 1
        elif key == "up":
            self.jump()

    def jump(self):
        if self.rect.bottom >= consts.WINDOW_SIZE[1]:
            self.change_y = -10

    def stop(self):
        self.change_x = 0

    def gravity_effect(self):

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


class Blue(Player):

    def __init__(self):
        super(Blue, self).__init__("gfx/person-blue.png", x=100)

