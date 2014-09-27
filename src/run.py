# -*- coding: utf-8 -*-

import pygame


import consts
import levels
import lose
import platforms
import players
import win


def start():
    pygame.init()

    screen = pygame.display.set_mode(consts.WINDOW_SIZE)
    _play_again = True
    while _play_again:
        status = levels.display_level(screen)
        if status == "Quit":
            print "Bye"
            _play_again = False
        elif status == "Win":
            win.display_screen(screen)
        elif status == "Lose":
            lose.display_screen(screen)


if __name__ == '__main__':
    start()
    pygame.quit()

