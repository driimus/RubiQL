import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Rubik-v0',
    entry_point='gym_rubik.envs:RubikEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)

register(
    id='RubikHell-v0',
    entry_point='gym_rubik.envs:RubikHellEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)