# -*- coding: utf-8 -*-

import pygame.font

import consts

def display_simple_message(screen, message):
    font = pygame.font.Font(consts.FONT_PATH, 36)
    text = font.render(message, 1, (10, 10, 10))
    background = pygame.Surface(screen.get_size()).convert()
    _BACKGROUND_COLOR = (250, 250, 250)
    background.fill(_BACKGROUND_COLOR)
    textpos = text.get_rect(
            centerx=background.get_width()/2,
            centery=background.get_height()/2
            )
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

