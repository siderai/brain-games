[![Actions Status](https://github.com/siderai/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/siderai/python-project-lvl1/actions) <a href="https://codeclimate.com/github/siderai/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/c8574923098dd1fdd82b/maintainability" /></a> ![example workflow](https://github.com/siderai/python-project-lvl1/actions/workflows/brain-games.yml/badge.svg)
# A package of five CLI calculus games

In every game you should answer three arithmetic questions. After a correct answer you pass to the next question, otherwise the game is over. 

KISS, DRY, YAGNI are applied to code style. Generally, this CLI app has 3 levels of abstraction, isolated from each other: script, engine and game logic. The executable scripts are divided from the logic of each game as well as from the game engine. The game engine itself is created to avoid repetitions in common gameplay parts: greeting, questioning, game summary.

Training project at hexlet.io.
## Tasks: 
1. Deploying and automation of dev environment (Linux, Make, Flake8, CC, CI)
2. Dependencies management (Poetry)
3. Git practice (GitHub)
4. Python packaging experience (PyPI)
5. Complexity management practice

## Stack:

Python3
• Poetry
• PyPI
• Linux
• Git
• Github Actions (CI)
• Flake8
• CodeClimate
• Make

## Quickstart:

``` 
git clone https://github.com/siderai/brain-games
cd brain-games
make package-install
```

## Games:
### $ brain-calc

Simple calculator game. Numbers and operators are selected randomly.

### $ brain-prime

Determine if the number is prime or not.

### $ brain-gcd

Find greatest common divisor for the random pair of numbers.
 
### $ brain-progression

Find the missing element of arithmetic progression. The length of progression is fixed by 10 elements, but the position of missing number and the step of progression are random.

### $ brain-even

Determine if the given number is even.
