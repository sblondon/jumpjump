# -*- coding: utf-8 -*-

import pygame.font
import pygame.time

import consts

def display_simple_message(screen, message, duration=consts.DEFAULT_DISPLAY_DURATION):
    font = pygame.font.Font(consts.FONT_PATH, 36)
    TEXT_COLOR = (10, 10, 10)
    text = font.render(message, True, TEXT_COLOR)
    background = pygame.Surface(screen.get_size()).convert()
    BACKGROUND_COLOR = (250, 250, 250)
    background.fill(BACKGROUND_COLOR)
    textpos = text.get_rect(
            centerx=background.get_width()/2,
            centery=background.get_height()/2
            )
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    pygame.time.delay(duration)

