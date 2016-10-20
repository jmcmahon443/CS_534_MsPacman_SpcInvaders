# CS_534_MsPacman
Reinforcement Learning for Ms. Pacman

## Installation Instructions
```
pip install gym
pip install gym[atari]
```

On OSX or maxOS:
```
brew install cmake boost boost-python sdl2 swig wget
```

On Ubuntu 14.04:
```
apt-get install -y python-numpy python-dev cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl libboost-all-dev libsdl2-dev swig
```

## Github
```
git clone https://github.com/jmcmahon443/CS_534_MsPacman.git
```

## Samples
```
python do_nothing.py
```
```
python random.py
```
```
python reinforcement_learning.py
```
```
python reinforcement_learning_with_difference_vector.py
```

## Agents
[See OpenAI example agents](https://github.com/openai/gym/tree/master/examples/agents)

Manually controlled agent
```
python manual.py
```

UCB Reinforcement
```
cd reinforcement_ucb
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 1 -n 10 -l originalClassic -g 'DirectionalGhost'
```
[RL Tutorials](http://ai.berkeley.edu/reinforcement.html)
