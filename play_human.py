from gym_cooking.misc.game.gameplay import GamePlay
from gym_cooking.envs.overcooked_environment import OvercookedEnvironment, MapSetting
from gym_cooking.utils.replay import Replay
import argparse
import pygame
import time
from copy import deepcopy
from gym_cooking.misc.game.input_id import id_input

import argparse
from datetime import datetime
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser("Overcooked argument parser")
    parser.add_argument(
        "--map", type=str,
        choices=MAP_SETTINGS.keys(),  # choicesにMAP_SETTINGSのキーを使用
        default='standard'
    )
    return parser.parse_args()

MAP_SETTINGS = dict(
    practice=dict(level="new1", num_agents=1,max_num_timesteps=200),
    ring=dict(level="new2",num_agents=1,max_num_timesteps=100),
    concave=dict(level="new3",max_num_timesteps=100),
    partition=dict(level="new4",max_num_timesteps=100),
    expand = dict(level="new5", order_plus = True,max_num_timesteps=100),
    standard=dict(level="new6", order_plus=True,max_num_timesteps=100),
)

def pair_map(map_name):
    today_str = datetime.now().strftime("%m%d")
    time_str = datetime.now().strftime("%H%M")

    player_ids = []
    for i in range(2):
        id = id_input(i)
        player_ids.append(id)

    player_id = '-'.join(player_ids)
        
    map_set = MapSetting(**MAP_SETTINGS[map_name])

    env = OvercookedEnvironment(map_set)
    env.reset()
        
    replay = Replay()
    replay['set_map'] = deepcopy(map_set)
    replay['order_rand'] = deepcopy(env.order_scheduler.rand_recipe_list)
    replay['chg_rand'] = deepcopy(env.chg_rand_list)
    replay['player_id'] = deepcopy(player_id)
    replay['map_name'] = deepcopy(map_name[:4])
        
    
    repdir = Path(__file__).resolve().parent /'gym_cooking'/ 'replay' / 'replay_log' / 'pair' / today_str / time_str

    repdir.mkdir(parents=True, exist_ok=True)

    game_setting = {"mode" : "pair", "map_name" : map_name, "player_number" : [0,1]}
    game = GamePlay(env,replay,game_setting)
    ok = game.on_execute(repdir)
  


def solo_map(map_name):
    today_str = datetime.now().strftime("%m%d")
    time_str = datetime.now().strftime("%H%M")
    
    player_id = id_input(0)    
    map_set = MapSetting(**MAP_SETTINGS[map_name])

    env = OvercookedEnvironment(map_set)
    env.reset()
    
    replay = Replay()
    replay['set_map'] = deepcopy(map_set)
    replay['order_rand'] = deepcopy(env.order_scheduler.rand_recipe_list)
    replay['chg_rand'] = deepcopy(env.chg_rand_list)
    replay['player_id'] = deepcopy(player_id)
    replay['map_name'] = deepcopy(map_name[:4])
    
    repdir = Path(__file__).resolve().parent/ 'gym_cooking' / 'replay' /  'replay_log' / 'single' / today_str / time_str
    repdir.mkdir(parents=True, exist_ok=True)
    
    game_setting = {"mode" : "solo", "map_name" : map_name, "player_number" : 0}
    game = GamePlay(env,replay,game_setting)
    ok = game.on_execute(repdir)


if __name__ == '__main__':
    arglist = parse_arguments()
    if arglist.map == 'practice' or arglist.map == "ring":
        solo_map(arglist.map)
    else:
        pair_map(arglist.map)

        
    




