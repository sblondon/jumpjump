# -*- coding: utf-8 -*-

import engine

def display_win(screen, game):
    won_levels = game.won_levels
    template = u"Team wins %d level :-)" if won_levels == 1 else u"Team wins %d levels :-)"
    message = template % won_levels
    engine.display_simple_message(screen, message)

