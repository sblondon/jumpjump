# -*- coding: utf-8 -*-
import pygame.display

import engine

def display_lose_level():
    engine.display_simple_message(u"Team fails! Try again...")

def display_lose_game(game):
    won_levels = game.won_levels
    template = u"Game over (won: %d level)" if won_levels == 1 else u"Game over (won: %d levels)"
    message = template % won_levels
    engine.display_simple_message(message)

