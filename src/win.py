# -*- coding: utf-8 -*-

import engine

def display_win(screen, game):
    win_games = game.won_games
    template = u"Team wins %d game :-)" if win_games == 1 else u"Team wins %d games :-)"
    message = template % win_games
    engine.display_simple_message(screen, message)

