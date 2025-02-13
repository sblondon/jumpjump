# -*- coding: utf-8 -*-
import pygame.display

import engine

def display_lose_level():
    engine.display_simple_message("Team fails! Try again...")

def display_lose_game(game):
    won_levels = game.won_levels
    plural_mark = "" if won_levels == 1 else "s"
    message = f"Game over (won: {won_levels} level{plural_mark})"
    engine.display_simple_message(message)

