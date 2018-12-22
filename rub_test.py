import gym.spaces
import gym_rubik


# 3x3 Rubik's Cube
env = gym.make("Rubik-v0")

print(env.reset()) # print status
env.render()

print(env.reset()) # scramble status
env.render()
env.step(0) # action 0~11
env.step(1) # action 0~11
env.render()
# scramble, action = env.getlog()
# print("Scramble: ", scramble)
# print("Action: ", action)


