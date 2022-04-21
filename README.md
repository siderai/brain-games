[![Actions Status](https://github.com/siderai/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/siderai/python-project-lvl1/actions) <a href="https://codeclimate.com/github/siderai/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/c8574923098dd1fdd82b/maintainability" /></a> ![example workflow](https://github.com/siderai/python-project-lvl1/actions/workflows/brain-games.yml/badge.svg)
# A package of five CLI calculus games

Insprired by mobile puzzle apps. In every game you should answer three arithmetic questions. After a correct answer you pass to the next question, otherwise the game is over.  All questions are randomly generated. 

KISS, DRY, YAGNI principles are applied to the project. The code base is organized in three levels of abstraction, isolated from each other: the game logic, the game engine and the scripts. Every game has it's own script running game logic through the engine. The engine itself was created to avoid repetitions in common gameplay parts: greeting, questioning, summary.

Training project at hexlet.io.

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

## Acquired skills: 
1. Deploying and automation of dev environment (Linux, Make, Flake8, CodeClimate, Github Actions)
2. Dependencies management (Poetry)
3. Git practice (GitHub, Linux)
4. Complexity management practice (Python, levels of abstraction)
5. Python packaging experience (PyPI)

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
