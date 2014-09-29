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
    _win_games = 0
    _lives = 3
    _play_again = True
    while _play_again:
        status = levels.display_level(screen, _lives)
        if status == "Quit":
            print "Bye"
            _play_again = False
        elif status == "Win":
            _win_games += 1
            win.display_win(screen, _win_games)
        elif status == "Lose":
            _lives -= 1
            if _lives == 0:
                lose.display_lose_game(screen)
                _win_games = 0
                _lives = 3
            else:
                lose.display_lose_level(screen)


if __name__ == '__main__':
    start()
    pygame.quit()

