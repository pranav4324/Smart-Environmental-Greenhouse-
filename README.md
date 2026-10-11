# Number Guessing Game (AI Logic)

A beginner-friendly Python project made for interviews. It includes two modes:

- **Player Guess Mode:** the computer picks a random number and the player guesses it.
- **AI Guess Mode:** the player thinks of a number and the computer guesses it using binary search.

This project demonstrates:

- Python basics: functions, classes, loops, conditionals, and input validation
- `random.randint()` for game behavior
- Binary search as a simple adaptive decision-making strategy
- A small test suite using Python's built-in `unittest`

## Why This Is an AI Logic Project

The AI mode does not guess randomly. It adapts after every response:

- If the guess is too low, it removes the lower half of possible values.
- If the guess is too high, it removes the upper half of possible values.
- It always guesses the middle of the remaining range.

For numbers from 1 to 100, the AI needs at most 7 guesses because:

```text
ceil(log2(100)) = 7
```

This is the same idea behind binary search in Data Structures and Algorithms.

## Project Structure

```text
Number Guessing Game AI/
├── number_guessing_game.py
├── README.md
└── tests/
    └── test_number_guessing_game.py
```

## How to Run

Open a terminal in this folder and run:

```bash
python number_guessing_game.py
```

On Windows, if `python` is not recognized, run:

```bash
py number_guessing_game.py
```

If you are in a different folder, run it with the full path:

```bash
py "D:\Project\Number Guessing Game AI\number_guessing_game.py"
```

You can also double-click:

```text
run_game.bat
```

## How to Run Tests

```bash
python -m unittest discover -s tests
```

Or on Windows:

```bash
py -m unittest discover -s tests
```

## Interview Explanation

You can explain it like this:

> I built a two-mode number guessing game in Python. In the first mode, the program generates a random number and the user guesses it. In the second mode, the program uses binary search logic to guess the user's number. After each response, the program updates its search range, which demonstrates adaptive decision-making. This helped me connect my DSA knowledge with a basic AI-style logic system.

## Future Improvements

- Add score history
- Add difficulty levels
- Add a GUI using Tkinter
- Add a smarter hint system for player mode
