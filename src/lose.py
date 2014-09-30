# -*- coding: utf-8 -*-
import pygame.display

import engine

def display_lose_level():
    screen = pygame.display.get_surface()
    engine.display_simple_message(screen, u"Team fails! Try again...")

def display_lose_game():
    screen = pygame.display.get_surface()
    engine.display_simple_message(screen, u"Game over")

