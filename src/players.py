# -*- coding: utf-8 -*-

import pygame


class Player(object):
    def __init__(self, image_path, x):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.speed = [0, 0]
        self.position = self.get_rect().move(x, 150)
        self.move_requested = {"down": False, "up": False, "left": False, "right": False}

    def get_rect(self):
        return self.image.get_rect()

    def move(self):
        if self.move_requested["up"]:
            self.speed[1] = -1
        if self.move_requested["right"]:
            self.speed[0] = 1
        if self.move_requested["down"]:
            self.speed[1] = 1
        if self.move_requested["left"]:
            self.speed[0] = -1

        self.position = self.position.move(self.speed)
        self.move_requested = {"down": False, "up": False, "left": False, "right": False}
        self.speed = [0, 0]

    def move_enable(self, key):
        self.move_requested[key] = True

    def should_move(self):
        return any(self.move_requested.values())


class Red(Player):
    def __init__(self):
        super(Red, self).__init__("gfx/person-red.png", x=50)


class Blue(Player):

    def __init__(self):
        super(Blue, self).__init__("gfx/person-blue.png", x=100)

