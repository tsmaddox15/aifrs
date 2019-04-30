# AIFRS - Artificial Intelligent Flight Radar Simulator
This README is a step-by-step guide for running the Spinning Up project and a partial working copy of a FrozenLake environment implementation.

# Steps for getting spinningup to train
- It's important to note, Ubuntu 18.0.4 was used for testing with ~100GB of virtual hard disk space.
- For guidance on setting up an Ubuntu 18.0.4 Virtual Machine, see the end of the document titled "Setting up an Ubuntu VM on VirtualBox"

## First, run apt-get update to make sure everything is up-to-date
sudo apt-get update

## Using Linux, install Anaconda for Python 3.7
- (https://docs.continuum.io/anaconda/install/linux)
- Download the installer
- In a terminal, enter the following to install Anaconda for Python 3.7:
  - bash ~/Downloads/Anaconda3-2019.03-Linux-x86_64.sh
		**Note:** The name of the .sh file may differ
- Follow default steps that come.

## Create a virtual environment (conda env) for organizing specific packages (you may need to restart your terminal)
- Enter the following to create and activate your Spinning Up virtual environment:
	- conda create -n spinningup python=3.6
	- source activate spinningup

## Install OpenMPI
- Run the following to install OpenMPI:
	sudo apt-get update && sudo apt-get install libopenmpi-dev

## Clone the Spinning Up repository from OpenAI's GitHub
- Run the following to download the Spinning Up repository:
	- git clone https://github.com/openai/spinningup.git
	- cd spinningup
	- pip install -e .
- This will install all necessary tools for running Spinning Up

## Test OpenAI by running PPO (Proximal Policy Optimization)
- Note that this initial run takes about 15 minutes.
- Run the following to train the Lunar Lander default model using OpenAI:
	- python -m spinup.run ppo --hid "[32,32]" --env LunarLander-v2 --exp_name installtest --gamma 0.999
- Watch the results by running the following (takes about a minute to load)
	- python -m spinup.run test_policy data/installtest/installtest_s0
- Plot results with the following:
	- python -m spinup.run plot data/installtest/installtest_s0

# Download Gym and get FrozenLake to run.
- Gym is a toolkit for developing and comparing RL algorithms
- We chose FrozenLake because it's close to our hunter-prey scenario

## Clone the gym repository
- Run the following to clone and install the Gym github repository
	- git clone https://github.com/tsmaddox15/aifrs.git
	- cd gym
	- pip install -e .
		**Note:** The pip install isn't needed if previously performed above

## Install necessary libraries for OpenAI
- Run the following to install the necessary tools/libraries for OpenAI
	- apt install -y python3-dev zlib1g-dev libjpeg-dev cmake swig python-pyglet python3-opengl libboost-all-dev libsdl2-dev libosmesa6-dev patchelf ffmpeg xvfb

    **Note:** ^The above is all one line. Not needed if previously done. It's not a bad idea to try running the scripts before installing all of these; if it fails, this is a good thing to do.

## Run the script to generate the Q-table
- cd into gym/gym/envs/toy_text
- run the following to gather the Q-table for the scenario
	- python q-table.py

## Run the script to run a simulation of the frozen lakes
- cd into gym/gym/envs/toy_text (if not already)
- run the following to run a simulation of frozen lakes:
	- python train-lakes.py

# Setting up an Ubuntu VM on VirtualBox
- Download VirtualBox for your specific operating system (https://www.virtualbox.org/wiki/Downloads)
- Download the Ubuntu 18.04 iso file (https://www.ubuntu.com/download/desktop)
- Once done downloading, open VirtualBox and select "New"
- You can name the VM whatever, we just named it Ubuntu
- Select the following:
  - Type: Linux
  - Version: Ubuntu (64-bit)
- Select next
- Select the amount of RAM used in the VM (We recommend the most possible in the green line. We used about 12k MB.)
- Select next
- Select "Create a virtual hard disk now"
- Select VDI for the hard disk file type
- Select "Fixed size" for the "Storage on physical hard disk"
- Enter ~100GB. We found the whole installation and building took up about 15 GB, but the more the merrier and safer.
- Select Create
- The first time opening the VM, you will have to install Ubuntu; the steps are straight forward from there.

# Useful links and notes
- Towards the tail end of our research, we found this to be interesting and possibly helpful for learning how OpenAI works and all.
  - https://www.youtube.com/watch?v=_pF1Un5zvp4
  - https://github.com/kengz/openai_lab
- We investigated the FrozenLake environment (https://gym.openai.com/envs/FrozenLake-v0/) because it's set up very similarly to the hunter/prey scenario we would like to emulate. We thought knowledge of this environment would help us with understanding how to set up a custom hunter/prey environment.
- Some useful links we found relating to FrozenLake environment:
  - https://medium.com/swlh/introduction-to-reinforcement-learning-coding-q-learning-part-3-9778366a41c0
  - https://www.analyticsindiamag.com/openai-gym-frozen-lake-beginners-guide-reinforcement-learning/
- The scripts we have for the FrozenLake attempts are located under gym/gym/envs/toy_text
- The documentation from OpenAI on creating custom environments: https://github.com/openai/gym/blob/master/docs/creating-environments.md
  - We were unsuccessful with this approach, but it may be helpful in the future.

# Questions?
- Email us at tsmaddox15@gmail.com or e.comte96@gmail.com
