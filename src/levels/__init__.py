from . import development
import engine
from . import progress    


def select_level(game):
    Level = progress.LEVELS.get(game.won_levels, progress.RandomLevel)
    return Level(game)

def introduce_level(game):
    msg = f"Level {game.won_levels + 1}"
    engine.display_simple_message(msg)

def select_testlevel(game):
    return development.TestLevel(game)

