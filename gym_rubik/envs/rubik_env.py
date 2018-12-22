import os, subprocess, time, signal
import gym
import numpy as np

from gym import error, spaces
from gym import utils
from gym.utils import seeding

from gym_rubik.envs import rubik
import logging
logger = logging.getLogger(__name__)

class RubikEnv(gym.Env, utils.EzPickle):
	
    metadata = {'render.modes': ['human']}
	
    def __init__(self, sideLength = 3, sides = 6):
        self.sideLength = sideLength
        self.sideCount = sides
        self.low = np.array([0 for i in range(self.sideLength*self.sideLength*self.sideCount)])
        self.high = np.array([5 for i in range(self.sideLength*self.sideLength*self.sideCount)])

        self.observation_space = spaces.Box(self.low, self.high, dtype= np.uint8)
        # Moveset omits axis rotations
        self.action_space = spaces.Discrete(12)

    def step(self, action):
        self.cube.handleInput(ACTION_LOOKUP[action])
        self.state = self.get_flat()
        
        self.step_count += 1
        
        reward = 0.0
        done = False
        others = {}
        
        if self.cube.isSolved():
            reward = 1.0
            done = True
            
        if self.step_count > 40:
            done = True
            
        
        return self.state, reward, done, others


    def _get_reward(self):
        """ Reward is given for completing a face. """
        if self.status == hfo_py.GOAL:
            return 1
        else:
            return 0
    
    def get_flat(self):
        return np.array([COLOR_DICT[i] for i in self.cube.flatten()])

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
	
    def reset(self):
        self.state = {}
        self.cube = rubik.Cube(3)
        self.cube.scramble()
        self.step_count = 0

        self.state = self.get_flat()
        return self.state

    def render(self, mode='human', close=False):
        if close:
            return
        else:
            self.cube.niceDisplay()

ACTION_LOOKUP = {
	0 : "U",
	1 : "U'",
	2 : "M",
	3 : "M'",  
	4 : "D",
	5 : "D'",
	6 : "R",
	7 : "R'",
	8 : "L",
	9 : "L'",
	10 : "F",
	11 : "F'"
}

COLOR_DICT = {
    'w' : 0,
    'r' : 1,
    'g' : 2,
    'o' : 3,
    'b' : 4,
    'y' : 5
}
