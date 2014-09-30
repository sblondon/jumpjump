# -*- coding: utf-8 -*-
import copy

import pygame

import consts
import engine
import games
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

    game = games.Game()
    while game.play_again:
        game = levels.display_level(screen, game)
        if game.status == "Quit":
            print "Bye"
            game.play_again = False
            game.status = None
        elif game.status == "Win":
            game.status = None
            win.display_win(screen, game)
        elif game.status == "Lose":
            game.status = None
            if game.lives == 0:
                lose.display_lose_game(screen)
                game.lives = 3
                game.won_games = 0
            else:
                lose.display_lose_level(screen)


if __name__ == '__main__':
    start()
    pygame.quit()

