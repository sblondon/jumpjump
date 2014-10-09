# -*- coding: utf-8 -*-

import development
import engine
import progress    


def select_level(game):
    LVLS = progress.LVLS
    _Level = LVLS.get(game.won_levels, progress.RandomLevel)
    return _Level(game)

def introduce_level(game):
    msg = u"Level %d" % (game.won_levels + 1)
    engine.display_simple_message(msg)

def select_testlevel(game):
    return development.TestLevel(game)

