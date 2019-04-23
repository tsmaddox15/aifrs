# AIFRS #

# Steps for getting spinningup to train
- It's important to note, Ubuntu 18.0.4 was used for testing with ~100GB of virtual hard disk space.

## First, run apt-get update to make sure everything is up-to-date
sudo apt-get update

## Using Linux, install Anaconda for Python 3.7
- (https://docs.continuum.io/anaconda/install/linux)
- Download the installer
- In a terminal, enter the following to install Anaconda for Python 3.7:
	bash ~/Downloads/Anaconda3-2019.03-Linux-x86_64.sh
		**Note:** The name of the .sh file may differ
- Follow default steps that come.

## Create a virtual environment (conda env) for organizing specific packages (you may need to restart your terminal)
- Enter the following to create and activate your Spinning Up virtual environment:
	conda create -n spinningup python=3.6
	source activate spinningup

## Install OpenMPI
- Run the following to install OpenMPI:
	sudo apt-get update && sudo apt-get install libopenmpi-dev

## Clone the Spinning Up repository from OpenAI's GitHub
- Run the following to download the Spinning Up repository:
	git clone https://github.com/openai/spinningup.git
	cd spinningup
	pip install -e .
- This will install all necessary tools for running Spinning Up

## Test OpenAI by running PPO (Proximal Policy Optimization)
- Note that this initial run takes about 15 minutes.
- Run the following to train the Lunar Lander default model using OpenAI:
	python -m spinup.run ppo --hid "[32,32]" --env LunarLander-v2 --exp_name installtest --gamma 0.999
- Watch the results by running the following (takes about a minute to load)
	python -m spinup.run test_policy data/installtest/installtest_s0
- Plot results with the following:
	python -m spinup.run plot data/installtest/installtest_s0




# Download Gym and get FrozenLake to run.
- Gym is a toolkit for developing and comparing RL algorithms
- We choose FrozenLake because it's close to our hunter-prey scenerio

## Clone the gym repository
- Run the following to clone and install the Gym github repository
	git clone https://EComte@bitbucket.org/gouph/aifrs.git
	cd gym
	pip install -e .
		**Note:** The pip install isn't needed if previously performed above

## Install necessary libraries for OpenAI
- Run the following to install the necessary tools/libraries for OpenAI
	apt install -y python3-dev zlib1g-dev libjpeg-dev cmake swig python-pyglet python3-opengl libboost-all-dev libsdl2-dev libosmesa6-dev patchelf ffmpeg xvfb
		**Note:** ^All one line. Not needed if previously done. It's not a bad idea to try running the scripts before installing all of these; if it fails, this is a good thing to do.

## Run the script to generate the Q-table
- cd into gym/gym/envs
- run the following to gather the Q-table for the scenario
	python q-table.py

## Run the script to run a simulation of the frozen lakes
- cd into gym/gym/envs (if not already)
- run the following to run a simulation of frozen lakes:
	python train-lakes.py
