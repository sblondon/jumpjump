# -*- coding: utf-8 -*-

import pygame

import games
import levels

WINDOW_SIZE = 640, 480


def run():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    game = games.Game()
    game.won_levels +=1
    level = levels.select_testlevel(game)
    game = level.play()


if __name__ == '__main__':
    run()
    pygame.quit()

