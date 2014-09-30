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
    game = {"won_games": 0, "lives": 3, "play_again": True, "status": None}
    while game["play_again"]:
        game = levels.display_level(screen, game)
        if game["status"] == "Quit":
            print "Bye"
            game["play_again"] = False
            game["status"] = None
        elif game["status"] == "Win":
            game["won_games"] += 1
            game["status"] = None
            win.display_win(screen, game["won_games"])
        elif game["status"] == "Lose":
            game["lives"] -= 1
            game["status"] = None
            if game["lives"] == 0:
                lose.display_lose_game(screen)
                game["won_games"] = 0
                game["lives"] = 3
            else:
                lose.display_lose_level(screen)


if __name__ == '__main__':
    start()
    pygame.quit()

