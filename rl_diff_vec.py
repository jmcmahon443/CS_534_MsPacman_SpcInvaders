import gym, os, io
import numpy as np

functionname, _ = os.path.splitext(__file__)
n = 0
filename = "analysis/"+functionname+str(n)+".csv"
while os.path.isfile(filename):
    n = n + 1
    filename = "analysis/"+functionname+str(n)+".csv"
print filename
with io.FileIO(filename, "w") as file:
    file.write("Episode, Score\n")

env = gym.make('MsPacman-v0')

def run_episode(env):
    observation = env.reset()
    reward_total = 0

    last_observation = 0
    parameters = np.random.rand(9, 100800)

    timesteps = 0
    for t in xrange(2000):
        env.render()
        
        observation = observation.reshape([100800, 1])

        diff_observation = observation - last_observation
        changed_pixels = np.transpose(np.nonzero(diff_observation))[:, 0]
        last_observation = observation

        score = np.matmul(parameters, diff_observation)         # calculate each action's score
        action = np.argmax(score)                               # choose the action with the highest score

        observation, reward, done, info = env.step(action)
        reward_total = reward_total + reward

        if done:
            timesteps = t + 1
            break
    return parameters, reward_total, timesteps

def train():
    num_episodes = 1000
    best_param = 0
    best_reward = 0
    average_reward = 0

    for e in xrange(1000):
        parameters, reward, timesteps = run_episode(env)

        print "Episode %d finished with score of %d after %d timesteps" % (e+1, reward, timesteps)
        with io.FileIO(filename, "a") as file:
            file.write("%d, %d, %d\n" % (e+1, reward, timesteps))

        if reward > best_reward:
            best_reward = reward
            best_param = parameters

    return best_param, best_reward

if __name__ == "__main__":
    p, r = train()
    print p
    print r
    run_episode(env, p)