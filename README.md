# OvercookedChatEnviroment  

<div style="display: flex; gap: 20px;">
  <img src="./images\OvercookedchatEnvironment.png" width="600" />
</div>


This repository provides the offline cooperative cooking game environment for human-human collaboration.
This testbed was used to collect the [OvercookedChat dataset](https://github.com/UEC-InabaLab/OvercookedChat), a Japanese human-human dialogue dataset from a real-time collaborative cooking game environment.

## 🖥️ Testbed : Overcooked Game

### Introduction

The testbed is based on [gym-cooking](https://github.com/rosewang2008/gym-cooking) (Wu, Sarah A., et al. "Too Many Cooks: Bayesian Inference for Coordinating Multi‐Agent Collaboration.") and [hierarchical language agent](https://github.com/HosnLS/Hierarchical-Language-Agent) (Jijia Liu, et al. "LLM-Powered Hierarchical Language Agent for Real-time Human-AI Coordination."). Some additional features are added to the testbed:

1. **New Ingredient**: Paprika has been added as a new ingredient alongside onion, tomato, and lettuce.

2. **New Cooking Method** : A frying pan is introduced as a 3.new cooking tool, in addition to the original pot.

3. **New Recipes** : 16 new dishes that involve paprika and frying-pan-based cooking have been implemented.

4. **Extended Interface** : Each order now includes visual information about the required ingredients and cooking methods, making task goals more transparent and easier to follow.

###   Interaction
Human player can play the game with keyboard. Each human player controls the movement of one character. 
The keys for movement are as follows:
- player1: `up`/`down`/`left`/`right`
- player2: `w`/`s`/`a`/`d` (only Pair mode)

In addition to keyboard input, the game also supports game controller input. Currently, only the D-pad (directional pad) on the controller is supported for character movement and interactions. The game is designed with PlayStation style controllers in mind.


## 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/UEC-InabaLab/OvercookedChatEnviroment.git
   cd  OvercookedChatEnviroment
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Play

### 1. Solo Play
This environment supports both solo play  and human-human cooperative play.
```bash
python play_human.py --map practice
```
- `map`: solo map can be `practice` or `ring` 


### 2. Pair Play

```bash
python play_human.py --map standard
```

- `map`: pair map can be `standard`, `partition`, `partition` or `expand`.

After playing a round, the replay will be saved in `gym_cooking\replay` folder.

### 3. Replay
The replay can be replayed by the following command:

```bash
python OvercookedChatEnviroment/replay_main.py 
```

After running the command, you will be prompted to enter the filename of the replay.
Once entered, the recorded gameplay will be played back at `2×` speed.


## 🧪 Tested Environment
- Confirmed to work on Python 3.10.12.

## 📄 Citation

If you find this repository useful, please cite the following paper:

```bibtex
@inproceedings{overcookedchat,
  title     = {Task Proficiency-Aware Dialogue Analysis
 in a Real-Time Cooking Game Environment},
  author    = {Kaito Nakae and Michimasa Inaba},
  booktitle = {Proceedings of the 26th Annual Meeting of the Special Interest Group on Discourse and Dialogue},
  year      = {2025},
  url       = {https://github.com/UEC-InabaLab/OvercookedChat}
}
```