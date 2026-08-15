# Python Snake Game

A classic Snake game built with Python using the built-in `turtle` graphics library. The project uses object-oriented programming to separate the snake, food, scoreboard, and main game logic into individual modules.

## Features

* Classic Snake gameplay
* Arrow-key movement controls
* Randomly spawning food
* Snake growth after eating food
* Score tracking
* Persistent high score saved between games
* Wall collision detection
* Snake-tail collision detection
* Automatic game reset after a collision

## Controls

Use the arrow keys to control the snake:

* **↑ Up Arrow** — Move up
* **↓ Down Arrow** — Move down
* **← Left Arrow** — Move left
* **→ Right Arrow** — Move right

The game prevents the snake from immediately reversing into itself.

## Project Structure

```text
Python-Snake-Game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── data.txt
└── README.md
```

### `main.py`

Runs the main game loop, creates the game window, listens for keyboard input, and handles collisions between the snake, food, walls, and tail.

### `snake.py`

Contains the `Snake` class responsible for:

* Creating the snake
* Moving the snake
* Changing direction
* Adding new body segments
* Resetting the snake after a collision

### `food.py`

Contains the `Food` class, which creates food and randomly moves it to a new position whenever the snake eats it.

### `scoreboard.py`

Contains the `Scoreboard` class responsible for displaying the current score and high score.

The high score is stored in `data.txt`, allowing it to persist after the program is closed.

### `data.txt`

Stores the player's current high score.

## How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository:

```bash
git clone https://github.com/bpetersen459/Python-Snake-Game.git
```

3. Navigate into the project folder:

```bash
cd Python-Snake-Game
```

4. Run the game:

```bash
python main.py
```

No external packages are required because the project uses Python's built-in `turtle` module.

## What I Practiced

This project helped me practice:

* Python object-oriented programming
* Classes and inheritance
* Working with multiple Python modules
* Event listeners and keyboard input
* Collision detection
* File reading and writing
* Game loops
* Managing object state

## Built With

* Python
* Python Turtle Graphics
