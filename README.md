[![Actions Status](https://github.com/siderai/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/siderai/python-project-lvl1/actions) <a href="https://codeclimate.com/github/siderai/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/c8574923098dd1fdd82b/maintainability" /></a> ![example workflow](https://github.com/siderai/python-project-lvl1/actions/workflows/brain-games.yml/badge.svg)
# A package of five CLI calculus games

In every game you should answer three arithmetic questions. After a correct answer you pass to the next question, otherwise the game is over. All the games were written seperately, and then rewritten to avoid repetitions (DRY). Thus, unique game logic was divided from common gameplay parts: greeting, questioning, summary. The most challenging task was to create this game engine (or constructor)
Project at hexlet.io. 
## Tasks: 
1. Deploying and automation of dev environment (Linux, Make)
2. Dependencies management (Poetry)
3. Git practice
4. Python packaging experience (PyPI)
5. Try out complexity management 

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
pip install git+https://github.com/siderai/brain-games.git 
```

## Games:
### $ brain-calc

Simple calculator game. Numbers and operators are selected randomly.

### $ brain-even

Define whether given number is even or not.

### $ brain-gcd

Find greatest common divisor for random pair of numbers.

### $ brain-prime

Define whether given number is prime or not.
 
### $ brain-progression

Find the missing element of arithmetic progression. The length of progression is fixed (10), but the position of missing element and progression step are random.
