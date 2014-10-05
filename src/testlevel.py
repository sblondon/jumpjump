# -*- coding: utf-8 -*-

import pygame

import games
import levels

WINDOW_SIZE = 640, 480


def run():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    game = games.Game()
    level = levels.TestLevel(game)
    game = level.play()


if __name__ == '__main__':
    run()
    pygame.quit()

