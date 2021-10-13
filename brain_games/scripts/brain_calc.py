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
    print('Hello, {}!'.format(name))
    correct_answers = 0
    print('What is the result of the expression?')
    while correct_answers < 3:
        number1 = random.randint(0, 20)
        number2 = random.randint(0, 20)
        operation = random.randint(0, 2)
        answer, value = ask(number1, number2, operation)
        if answer == value:
            correct_answers += 1
            print('Correct!')
            if correct_answers == 3:
                print('Congratulations, {}!'.format(name))
        else:
            print('"{}" is wrong answer ;(. '.format(answer),
                  'Correct answer was "{}"'.format(value))
            print('Let\'s try again, {}!'.format(name))
            break


def ask(num1, num2, operator):
    if operator == 0:
        quest = 'Question: {} + {} = '.format(num1, num2)
        value = add(num1, num2)
    elif operator == 1:
        quest = 'Question: {} - {} = '.format(num1, num2)
        value = sub(num1, num2)
    elif operator == 2:
        quest = 'Question: {} x {} = '.format(num1, num2)
        value = mul(num1, num2)
    answer = int(prompt.string(quest, empty=True))
    return answer, value
