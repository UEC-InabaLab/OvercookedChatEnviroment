# modules for game
from gym_cooking.misc.game.game import Game
from gym_cooking.misc.game.utils import *
from gym_cooking.utils.gui import popup_text_source
from gym_cooking.utils.replay import Replay
import numpy as np
import os


# helpers
import pygame
import threading
import queue
from datetime import datetime
from pathlib import Path
from copy import deepcopy as dcopy


class GamePlay(Game):
    def __init__(self, env, replay:Replay, setting:dict):
        Game.__init__(self, env, play=True)
        # fps
        self.fps = 40
        self.replay = replay
        self._success = False

        self._q_control = queue.Queue()
        self._q_env = queue.Queue()
        self.render_queue = queue.Queue()

        self.stop_flag = threading.Event()  
        self.start_time = 0

        self.color_screen = (255,245,225)
        self.mode = setting['mode']
        self.map_name = setting['map_name']
        self.set_contorl(self.mode, setting['player_number'])

    def set_contorl(self, mode,player_number=None):
        print(f"Connected controllers num:{pygame.joystick.get_count()}")

    
        if mode == "pair":
            if pygame.joystick.get_count() > 1:
                for i in range(pygame.joystick.get_count()):
                    joystick = pygame.joystick.Joystick(i)
                    joystick.init()  
            
                if len(player_number) == 2:
                    self.id1 = player_number[0]
                    self.id2 = player_number[1]

                    self.joystick1 = pygame.joystick.Joystick(self.id1)
                    self.joystick2 = pygame.joystick.Joystick(self.id2)
                    self.joystick1.init()
                    self.joystick2.init()
                else:
                    raise ValueError("player number not 2")
            
        elif mode == "solo":
            if pygame.joystick.get_count() > 1:
                if isinstance(player_number, int):
                    self.id1 = player_number
                    self.joystick1 = pygame.joystick.Joystick(player_number)
                    self.joystick1.init()
                else:
                    raise ValueError("player number not 1")
               

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._q_control.put(('Quit', {}))

        elif event.type == pygame.KEYDOWN:
            if event.key in KeyToTuple.keys():
                # Control
                action_dict = {agent.name: (0, 0) for agent in self.sim_agents}
                action = KeyToTuple[event.key]
                action_dict[self.current_agent.name] = action
                self._q_env.put(('Action', {"agent": "1", "action": action}))

            if event.key in KeyToTuple2.keys():
                # Control
                action_dict = {agent.name: (0, 0) for agent in self.sim_agents}
                action = KeyToTuple2[event.key]
                action_dict[self.current_agent.name] = action
                self._q_env.put(('Action', {"agent": "2", "action": action}))

            if pygame.key.name(event.key) == "space":
                self._q_env.put(('Pause', {})) 

                s = popup_text_source("Say:")

                if s is not None:
                    self._q_env.put(('ChatIn', {"chat": s, "mode": "text"}))

                self._q_env.put(('Continue', {}))
   
        elif event.type == pygame.JOYHATMOTION:
            if event.joy == self.id1:
                hat_x, hat_y = self.joystick1.get_hat(0)
                self._q_env.put(('Action', {"agent": "1", "action": (hat_x , hat_y * -1)}))
            else:
                hat_x, hat_y = self.joystick2.get_hat(0)
                self._q_env.put(('Action', {"agent": "2", "action": (hat_x , hat_y * -1)}))

        elif event.type == pygame.JOYBUTTONDOWN:
            button = event.button
            if event.joy == self.id1:
                if button == 11:
                    self._q_env.put(('Action', {"agent": "1", "action": (0, -1)}))
                elif button == 12: 
                    self._q_env.put(('Action', {"agent": "1", "action": (0, 1)}))
                elif button == 13: 
                    self._q_env.put(('Action', {"agent": "1", "action": (-1, 0)}))
                elif button == 14: 
                    self._q_env.put(('Action', {"agent": "1", "action": (1, 0)}))
            elif event.joy == self.id2:
                if button == 11:
                    self._q_env.put(('Action', {"agent": "2", "action": (0, -1)}))
                elif button == 12:
                    self._q_env.put(('Action', {"agent": "2", "action": (0, 1)}))
                elif button == 13:
                    self._q_env.put(('Action', {"agent": "2", "action": (-1, 0)}))
                elif button == 14:
                    self._q_env.put(('Action', {"agent": "2", "action": (1, 0)}))
    
    def _run_env(self):
        action_dict = {agent.name: None for agent in self.sim_agents}
        chat = ''
        paused = False
        
        self.render_queue.put({
            'paused': paused, 
            'chat': chat,
            'type': 'render'
        })
        clock = pygame.time.Clock()
        while True:
            while not self._q_env.empty():
                event = self._q_env.get_nowait()
                event_type, args = event
                if event_type == 'Action':
                    if args['agent'] == "1":
                        action_dict[self.sim_agents[0].name] = args['action']
                    elif args['agent'] == "2":
                        action_dict[self.sim_agents[1].name] = args['action']
                elif event_type == 'Pause':
                    paused += 1
                elif event_type == 'Continue':
                    paused -= 1
                elif event_type == 'ChatIn':
                    chat = args['chat']

            delta_time = clock.tick(self.fps) / 1000.0
    
            if not paused:
                ad = {k: v if v is not None else (0, 0) for k, v in action_dict.items()}
                _, _, done, _ = self.env.step(ad, passed_time=delta_time)
                self.replay.log(
                    'env.step', {'action_dict': ad, 'passed_time': delta_time})
                
                if done:
                    self._success = True
                    self.render_queue.put({'type': 'quit'})
                    self.stop_flag.set()
                    return

                action_dict = {agent.name: None for agent in self.sim_agents}

            if not paused:
                self.replay.log('on_render', {'paused': paused, 'chat': chat})
            
            self.render_queue.put({
                'paused': paused, 
                'chat': chat,
                'type': 'render'
            })

    def _run_human(self):
        while True:
            if hasattr(self, 'render_queue'):
                while not self.render_queue.empty():
                    render_info = self.render_queue.get_nowait()
                    
                    if render_info['type'] == 'quit':
                        return
                    
                    if render_info['type'] == 'render':
                        self.on_render(
                            paused=render_info['paused'], 
                            chat=render_info['chat']
                        )

            for event in pygame.event.get():
                self.on_event(event)
            
            if not self._q_control.empty():
                event, args = self._q_control.get_nowait()
                if event == 'Quit':
                    return

    def show_opening_screen(self):
        self.screen.fill(self.color_screen)
            
        title_text = self.start_font_middle.render("協力型料理ゲーム", True, self.BLACK)
        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 4))
        self.screen.blit(title_text, title_rect)

        map_text = self.start_font_middle.render(f"マップ:{self.map_name.capitalize()}", True, self.BLACK)
        map_rect = map_text.get_rect(center=(self.width // 2, self.height // 4 + 100))
        self.screen.blit(map_text, map_rect)
            
        pygame.draw.rect(self.screen, self.GREEN, self.start_button_rect)
        start_text = self.start_font_small.render("Ⓧボタン・Enterでスタート!", True, self.BLACK)
        start_text_rect = start_text.get_rect(center=self.start_button_rect.center)
        self.screen.blit(start_text, start_text_rect)     

    def opeing_handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_RETURN: 
                        self.game_started = True
                        self.running = False

                elif event.type == pygame.JOYBUTTONDOWN:
                    button = event.button
                    if button == 0 :
                        self.game_started = True
                        self.running = False
                    

    def opening_screen(self):
            while self.running:
                self.opeing_handle_events()
                self.show_opening_screen()
                
                pygame.display.flip()
            

            if self.game_started:
                print("Game started!")

    def show_game_over_screen(self):
        self.screen.fill(self.color_screen)

      
        success_text = self.start_font_middle.render(f"提供できた注文: {self.env.order_scheduler.successful_orders}", True, self.BLACK)
        fail_text = self.start_font_middle.render(f"失敗した注文: {self.env.order_scheduler.failed_orders}", True, self.BLACK)
        reward_text = self.start_font_middle.render(f"合計スコア: {self.env.order_scheduler.reward}", True, self.BLACK)
        
        if self.mode == "pair":
            self.screen.blit(success_text, (self.width // 2 - success_text.get_width() // 2, self.height // 2 - 60))
            self.screen.blit(fail_text, (self.width // 2 - fail_text.get_width() // 2, self.height // 2))
            self.screen.blit(reward_text, (self.width // 2 - reward_text.get_width() // 2, self.height // 2 + 60))

        
        elif self.mode == "solo":
            self.screen.blit(success_text, (self.width // 2 - success_text.get_width() // 2, self.height // 2 - 60))
            self.screen.blit(fail_text, (self.width // 2 - fail_text.get_width() // 2, self.height // 2))
            self.screen.blit(reward_text, (self.width // 2 - reward_text.get_width() // 2, self.height // 2 + 60))


    def end_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RETURN: 
                        self.game_started = True
                        self.running = False
                
                elif event.type == pygame.JOYBUTTONDOWN:
                    button = event.button
                    if button == 0 :
                        self.game_started = True
                        self.running = False

    def end_step(self):
        while self.running:
                self.end_events()
                self.show_game_over_screen()
                
                pygame.display.flip()
            
        if self.game_end:
            print("Game started!")


    def on_execute(self, save_path=Path.cwd()):
        if self.on_init() == False:
            exit()
        
        self.save_path = save_path
        self.render_queue = queue.Queue() 
        self.stop_flag.clear() 

        self.opening_screen()
        

        thread_env = threading.Thread(target=self._run_env, daemon=True)
        thread_env.start()
        self._run_human()
        
        self.replay['order_result'] = dict(
            success=self.env.order_scheduler.successful_orders,
            fail=self.env.order_scheduler.failed_orders,
            reward=self.env.order_scheduler.reward,
        )

        self.replay.save(self.save_path / f'{self.replay["map_name"]}-{self.replay["player_id"]}-{datetime.now().strftime("%H%M")}.rep')

        self.running = True
        self.end_step()

        self.on_cleanup() 

        return self._success

    