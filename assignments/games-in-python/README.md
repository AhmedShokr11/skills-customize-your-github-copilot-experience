
# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## � What You'll Build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:

# 📘 Assignment: Games in Python — Hangman

**Due Date:** 2025-11-16
**Path:** assignments/games-in-python

## 🎯 Objective

Build a playable Hangman game in Python that practices string manipulation, conditionals, loops, and basic user I/O.

## 🎯 Learning Outcomes

- Use lists and strings to manage game state
- Implement control flow with loops and conditionals
- Read input and provide clear console feedback
- Structure code into functions for clarity and reuse

## 📝 Tasks

### 🛠️ Task 1 — Core Hangman

#### Description
Implement the basic Hangman game loop: choose a word, accept letter guesses, reveal progress, and track remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses and ignore repeated guesses
- Display the current word progress (e.g. H _ N G M A N)
- Track and display remaining incorrect attempts
- End when the word is fully guessed or attempts reach zero
- Show a clear win or lose message with the correct word

### 🛠️ Task 2 — Optional Extensions (extra credit)

#### Description
Add one or more enhancements to improve gameplay, robustness, or usability.

#### Examples (pick any)

- Add difficulty levels that change allowed attempts or word lists
- Load words from an external file (e.g. `words.txt`) or `data.csv`
- Implement a scoring system or high-score persistence
- Add ASCII-art hangman stages or a simple GUI (e.g. `curses` or `tkinter`)

## 🧰 Starter files

- `starter-code.py` — minimal skeleton to get started (edit and run locally)

To run the starter script locally:

```bash
python3 assignments/games-in-python/starter-code.py
```

## ✅ Submission

Place your final `.py` file(s) in the `assignments/games-in-python/` folder or provide a downloadable archive. Include a short README describing any extra features you added.

## Help & Hints

- Validate input: accept only single alphabetic characters
- Keep game logic in functions to make testing easier
- Use the `random.choice()` function to select words
