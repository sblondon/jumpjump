# -*- coding: utf-8 -*-

import pygame

import consts
import engine
import games
import levels
import lose

WINDOW_SIZE = 640, 480


def run():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    engine.display_simple_message("JumpJump", duration=consts.SHORT_DISPLAY_DURATION)

    game = games.Game()
    while game.play_again:
        levels.introduce_level(game)
        level = levels.select_level(game)
        game = level.play()
        if game.status == "Quit":
            print("Bye")
            game.play_again = False
            game.status = None
        elif game.status == "Win":
            game.status = None
        elif game.status == "Lose":
            game.status = None
            if game.lives == 0:
                lose.display_lose_game(game)
                game.reset()
            else:
                lose.display_lose_level()


if __name__ == '__main__':
    run()
    pygame.quit()

