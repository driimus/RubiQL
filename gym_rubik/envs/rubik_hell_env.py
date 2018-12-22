import os, subprocess, time, signal
import gym
import numpy as np

from gym import error, spaces
from gym import utils
from gym.utils import seeding

import logging
logger = logging.getLogger(__name__)

class RubikHellEnv(gym.Env, utils.EzPickle):
    metadata = {'render.modes': ['human']}

    def __init__(self, sideLength = 3, sides = 6):
		self.sideLength = sideLength
		self.sideCount = sides
		self.low = np.array([0 for i in range(self.sideLength*self.sideLength*self.sideCount)])
		self.high = np.array([5 for i in range(self.sideLength*self.sideLength*self.sideCount)])

		self.observation_space = spaces.Box(low, high,)
        # Moveset omits axis rotations
        self.action_space = spaces.Discrete(12)

    def _step(self, action):
        ACTION_LOOKUP[action]()
		self.state = self._get_flat()
		
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
	
	def _get_flat(self):
		return np.array([COLOR_DICT[i] for i in self.cube.flatten()])

	def _reset(self):
		self.state = {}
        self.cube = rubik.Cube(3)
		self.cube.scramble()
		self.step_count = 0

		self.state = self._get_flat()
		return self.state

    def _render(self, mode='human', close=False):
        if close:
            return
        else:
            self.cube.niceDisplay()

ACTION_LOOKUP = {
    0 : self.cube.moveU,
    1 : self.cube.revU,
    2 : self.cube.moveM,
    3 : self.cube.revM,  
    4 : self.cube.moveD,
    5 : self.cube.revD,
    6 : self.cube.moveR,
    7 : self.cube.revR,
    8 : self.cube.moveL,
    9 : self.cube.revL,
    10 : self.cube.moveF,
    11 : self.cube.revF
}
COLOR_DICT = {
	'w' : 0,
	'r' : 1,
	'g' : 2,
	'o' : 3,
	'b' : 4,
	'y' : 5
}
