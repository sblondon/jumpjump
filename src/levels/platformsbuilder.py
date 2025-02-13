import random


def platform0_builder(level):
    level.create_default_platform(350, 50)
    level.create_default_platform(350, 100)
    level.create_goal(400, 400)


def platform1_builder(level):
    level.create_default_platform(300, 350)
    level.create_teleportable_goal(500, 400)


def platform2_builder(level):
    level.create_default_platform(200, 420)
    level.create_goal(300, 350)


def platform3_builder(level):
    level.create_default_platform(250, 420)
    level.create_goal(250, 300)


def platform4_builder(level):
    level.create_octopus_platform(250, 420)
    level.create_goal(250, 300)


def random_builder(level):
    platform_builder = random.choice ( (platform0_builder, platform1_builder, platform2_builder, platform3_builder, platform4_builder))
    platform_builder(level)
    level.goal.player_touch_required = level.game.won_levels

