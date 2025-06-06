This repository contains the **final version** of a Python text-based adventure game that uses an XML file to drive game content. It was created to help students in CSE 20 (and other beginner Python courses) learn how to combine Python logic with external data using XML.

If you're a student learning Python, this README will walk you through how to write your own version of this game step-by-step using the concepts you're learning in class.

---

## What You'll Learn by Building This Game

By building this game yourself, you will practice:

- Reading structured data using `xml.etree.ElementTree`
- Writing Python functions and organizing code in modules
- Validating user input using `try`/`except`
- Looping through prompts and managing game state with variables
- Structuring a program to use external data (XML) instead of hardcoding content
- Using the terminal to run Python programs with arguments

---

## Project Overview

This game is a **choose-your-own-adventure** style story. Players are presented with story prompts and must choose between two options. Each choice leads to a different outcome defined in an XML file. The game keeps track of the player’s name, score, and remaining lives.

---

## Files in This Repository

- `main.py`: The main program file that starts the game.
- `AdventureGame.py`: The game engine that loads and processes the XML, handles gameplay, and manages score and lives.
- `prompts.xml`: An external XML file that defines all story prompts and choices.
- `README.md`: Instructions (this file).
- `starter/`: A folder with empty template files you can use to start building your own version.

---

## How to Build the Game Yourself (Step-by-Step)

You should try to **write the code yourself** before looking at the full version in this repo.

### Step 1 – Set Up the Project

Create a folder with three empty files:

- `main.py`
- `AdventureGame.py`
- `prompts.xml`


### Step 2 – Build Your Code

### PSEUDOCODE:

# -----------------------------
# FILE 1: prompts.xml (game story)
# -----------------------------

# Create an XML file that holds your game prompts and options
# Structure should look like:

<prompts>
  <prompt id="start">
    <text>Welcome to your first challenge. Do you go left or right?</text>
    <option next="left_path">Go left</option>
    <option next="right_path">Go right</option>
  </prompt>

  <prompt id="left_path">
    <text>You encounter a river. Swim or build a raft?</text>
    <option next="swim_fail">Swim</option>
    <option next="raft_success">Build a raft</option>
  </prompt>

  <!-- Add more prompts and outcomes -->
</prompts>

# -----------------------------
# FILE 2: AdventureGame.py (game engine)
# -----------------------------

# Class: AdventureGame
# - load XML file
# - store prompts in a dictionary (key = id)
# - display prompts and get user input
# - update lives and score
# - end game if lives = 0 or no options left

# -----------------------------
# FILE 3: main.py (program entry point)
# -----------------------------

# Check if user provided XML file in command line
# If not → print usage and exit

# Create AdventureGame object with XML file
# Call game.play()

# -----------------------------
# EXTRA (Optional)
# -----------------------------

# Add ANSI color formatting to welcome text
# Cap max lives based on number of unique stages
# Add try/except for file not found or XML errors
# Add replay option at the end


-------------------------------

## How to Run the Game in This Repo

1. Make sure all 3 files (`main.py`, `AdventureGame.py`, and `prompts.xml`) are in the same folder.
2. Open a terminal and navigate to that folder.
3. Run the game with:

```bash
python3 main.py prompts.xml


