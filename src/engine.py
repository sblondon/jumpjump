# -*- coding: utf-8 -*-
import os.path

import pygame.font
import pygame.time

import consts

def display_simple_message(message, duration=consts.DEFAULT_DISPLAY_DURATION):
    screen = pygame.display.get_surface()
    text = build_message(message)
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

def build_message(message, text_color=(10, 10, 10)):
    font = pygame.font.Font(font_path(consts.FONT_NAME), 36)
    return font.render(message, True, text_color)


def image_path(filename):
    return os.path.join("assets", "gfx", filename)

def font_path(filename):
    return os.path.join("assets", "fonts", filename)

