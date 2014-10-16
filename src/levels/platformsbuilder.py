def level0_builder(level):
    level.create_default_platform(350, 50)
    level.create_default_platform(350, 100)
    level.create_goal(400, 400)


def level1_builder(level):
    level.create_default_platform(300, 350)
    level.create_teleportable_goal(500, 400)


def level2_builder(level):
    level.create_default_platform(200, 420)
    level.create_goal(300, 350)


def level3_builder(level):
    level.create_default_platform(250, 420)
    level.create_goal(250, 300)


def level4_builder(level):
    level.create_octopus_platform(250, 420)
    level.create_goal(250, 300)


def random_builder(level):
    level.create_octopus_platform(250, 420)
    goal = level.create_goal(250, 300)
    goal.player_touch_required = level.game.won_levels

