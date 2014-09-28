# -*- coding: utf-8 -*-

import pygame.time

import consts
import engine

def display_win(screen):
    engine.display_simple_message(screen, "Team wins! :-)")
    pygame.time.delay(consts.FIVE_SECONDS)

