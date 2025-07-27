from gym_cooking.misc.game.gamereplay import GamePlayReply
from gym_cooking.utils.gui import *
from gym_cooking.utils.replay import Replay
from gym_cooking.envs.overcooked_environment import OvercookedEnvironment, MapSetting

import argparse
from datetime import datetime
from pathlib import Path
import os 


def init_env_replay(replay):
    map_set = replay['set_map']
    print(replay['order_result'])
    env = OvercookedEnvironment(map_set)
    env.reset()
    env.order_scheduler.assign_rand_recipe_list(replay['order_rand'])  # 注文データの抽出
    env.assign_chg_rand_list(replay['chg_rand'])

    game = GamePlayReply(env, replay)

    return game, env, replay


if __name__ == '__main__':
    replay_filename = input("Enter replay filename: ")
    repdir = Path(__file__).resolve().parent / 'replay'
    replay = Replay.from_file(repdir / replay_filename)
    
    # initialize replay
    game, env, replay = init_env_replay(replay)

    # play
    game.on_execute()