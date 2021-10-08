#!/usr/bin/env python
import random
import prompt
from operator import add
from operator import sub
from operator import mul


def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    correct_answers = 0
    print('What is the result of the expression?')
    while correct_answers < 3:
        number1 = random.randint(0, 20)
        number2 = random.randint(0, 20)
        operation = random.randint(0, 2)
        if operation == 0:
            quest = 'Question: {} + {} = '.format(number1, number2)
            value = add(number1, number2)
        elif operation == 1:
            quest = 'Question: {} - {} = '.format(number1, number2)
            value = sub(number1, number2)
        elif operation == 2:
            quest = 'Question: {} x {} = '.format(number1, number2)
            value = mul(number1, number2)
        answer = int(prompt.string(quest, empty=True))
        if answer == value:
            correct_answers += 1
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}"'.format(answer, value))
            print('Let\'s try again, {}!'.format(name))
            break

    if correct_answers == 3:
        print('Congratulations, {}!'.format(name))
