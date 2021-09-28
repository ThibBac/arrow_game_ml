import gym
import pygame
import random
import numpy as np
from gym import spaces


class CustomEnv(gym.Env):
    def __init__(self, env_config={}):

        self.img_up = pygame.image.load("img/up.png")
        self.img_down = pygame.image.load("img/down.png")
        self.img_left = pygame.image.load("img/left.png")
        self.img_right = pygame.image.load("img/right.png")
        self.grid_size = 16
        self.game_dict = {}
        self.direction_dict = {1: self.img_up,
                               2: self.img_right,
                               3: self.img_down,
                               4: self.img_left}

        self.observation_space = spaces.Box(low=1, high=4, shape=(self.grid_size,),
                                            dtype=np.uint8)  # observation like [2, 1, 2, 3, 1, 3, ..., 1, 3, 3, 1]
        self.action_space = spaces.Discrete(self.grid_size)  # action 0 to 15

        self.init_render()

        self.n_steps = 0
        self.max_n_steps = 1000

    def init_render(self):
        pygame.init()
        self.window = pygame.display.set_mode((555, 755))
        self.clock = pygame.time.Clock()

        for i in range(4):
            for j in range(4):
                choice = random.choice(list(self.direction_dict.keys()))
                self.game_dict[(i, j)] = {'pos_x': i * 135 + (i * 5),
                                          'pos_y': j * 135 + (j * 5) + 200,
                                          'direction': choice}

                self.window.blit(self.direction_dict[self.game_dict[(i, j)]['direction']],
                                 (self.game_dict[(i, j)]['pos_x'], self.game_dict[(i, j)]['pos_y']))
                pygame.display.update()

    def reset(self):
        self.n_steps = 0

        for i in range(4):
            for j in range(4):
                choice = random.choice(list(self.direction_dict.keys()))
                self.game_dict[(i, j)] = {'pos_x': i * 135 + (i * 5),
                                          'pos_y': j * 135 + (j * 5) + 200,
                                          'direction': choice}

                self.window.blit(self.direction_dict[self.game_dict[(i, j)]['direction']],
                                 (self.game_dict[(i, j)]['pos_x'], self.game_dict[(i, j)]['pos_y']))

        observation = np.array([self.game_dict[i]['direction'] for i in self.game_dict], dtype=np.uint8)
        return observation

    def step(self, action=0):

        case_coord_i = action % 4
        case_coord_j = action // 4

        for i in range(case_coord_i - 1, case_coord_i + 2):
            for j in range(case_coord_j - 1, case_coord_j + 2):
                if (i, j) in self.game_dict.keys():
                    self.game_dict[(i, j)]['direction'] = self.game_dict[(i, j)]['direction'] % 4 + 1

        self.n_steps += 1

        observation = np.array([self.game_dict[i]['direction'] for i in self.game_dict], dtype=np.uint8)
        reward = 2 ^ int(np.count_nonzero(observation == 1))

        done = sum(observation) == self.grid_size
        if self.n_steps == self.max_n_steps - 1:
            done = True
            reward -= 20
        info = {}
        return observation, reward, done, info

    def render(self, mode='human'):
        self.window.fill((0, 0, 0))

        for (i, j), item in self.game_dict.items():
            self.window.blit(self.direction_dict[item['direction']], (i * 135 + (i * 5), j * 135 + (j * 5) + 200))
            pygame.display.update()
