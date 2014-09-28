# -*- coding: utf-8 -*-

import pygame.time

import consts
import engine

def display_lose(screen):
    engine.display_simple_message(screen, "Team fails! Try again...")
    pygame.time.delay(consts.FIVE_SECONDS)

