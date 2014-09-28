# -*- coding: utf-8 -*-

import pygame

import consts
import engine
import levels
import lose
import platforms
import players
import win

WINDOW_SIZE = 640, 480

def start():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    engine.display_simple_message(screen, "JumpJump", duration=consts.SHORT_DISPLAY_DURATION)
    _play_again = True
    while _play_again:
        status = levels.display_level(screen)
        if status == "Quit":
            print "Bye"
            _play_again = False
        elif status == "Win":
            win.display_win(screen)
        elif status == "Lose":
            lose.display_lose(screen)


if __name__ == '__main__':
    start()
    pygame.quit()

