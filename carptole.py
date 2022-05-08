import gym
import numpy as np

env = gym.make("CartPole-v0")

def Qtable(state_vars, actions, bin_size=30):
    '''
    Routine that returns a Q-Table and bin values of each state for the environment
    '''
    bins = [
        np.linspace(-4.8, 4.8, bin_size),
        np.linspace(-3, 3, bin_size),
        np.linspace(-0.418, 0.418, bin_size),
        np.linspace(-3, 3, bin_size),
    ]

    q_table = np.random.uniform(low=-1, high=1, size=([bin_size]*state_vars + [actions])) 

    return q_table, bins

def Discrete(state, bins):
    '''
    Routine that discretizes a state according to the Q-Table
    '''
    index = []
    for i in range(len(state)):
        index.append(np.digitize(state[i], bins[i]) - 1)
    return tuple(index)


# creating a qtable
qTable, bins = Qtable(
    len(env.observation_space.low), # or .high, doesn't really matter
    env.action_space.n
)


def Q(qTable, bins, episodes=5000, gamma=0.95, eta=0.1, timestep=1000, epsilon=0.15):
    rewards = 0
    steps = 0
    runs = [0]
    data = {'max': [0], 'avg': [0]}
    solved = False

    for episode in range(1, episodes+1):
        currentState = Discrete(env.reset(), bins)
        score = 0
        done = False

        while not done:
            steps += 1

            if episode%episodes == 0:
                env.render()

            # checking to see whether to explore or exploit
            if np.random.uniform(0,1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(qTable[currentState])

            # getting new state
            obs, reward, done, _ = env.step(action)
            newState = Discrete(obs, bins)

            # increasing the reward
            score += reward
            
            # updating the Qtable
            if not done:
                maxFutureQ = np.max(qTable[newState])
                currentQ = qTable[currentState + (action,)]
                newQ = (1-eta)*currentQ + eta*(reward + gamma*maxFutureQ)
                qTable[currentState + (action,)] = newQ

            currentState = newState

        else:
            rewards += score
            runs.append(score)
            if score > 195 and steps >= 100 and solved == False: # considered as a solved:
                solved = True
                print('Solved in episode : {}'.format(episode))
        
        # Timestep value update
        if episode % timestep == 0:
            print('Episode : {} | Reward -> {} | Max reward : {}'.format(episode,rewards/timestep, max(runs)))
            data['max'].append(max(runs))
            data['avg'].append(rewards/timestep)
            if rewards/timestep >= 195: 
                print('Solved in episode : {}'.format(episode))
            rewards, runs= 0, [0]


q_table, bins = Qtable(len(env.observation_space.low), env.action_space.n, bin_size=25)

Q(q_table, bins, eta=0.15, gamma=0.995, episodes=5*10**3, timestep=1000)

input()