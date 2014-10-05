# -*- coding: utf-8 -*-

import engine
import progress    


def select_level(game):
    LVLS = {0: progress.Level0,
            1: progress.Level1,
            2: progress.Level2,
            3: progress.Level3,
            }
    HigherLevel = LVLS[max(LVLS.keys())]
    _Level = LVLS.get(game.won_levels, HigherLevel)
    return _Level(game)

def introduce_level(game):
    msg = u"Level %d" % (game.won_levels + 1)
    engine.display_simple_message(msg)

def select_testlevel(game):
    return progress.TestLevel(game)

