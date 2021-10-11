import random
from math import gcd
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
            print('May I have your name? ', end='')
            name = input()
    print('Hello, {}!'.format(name))
    correct_answers = 0
    print('Find the greatest common divisor of given numbers.')
    while correct_answers < 3:
        number1 = random.randint(0, 40)
        number2 = random.randint(0, 40)
        quest = 'Question: ' + str(number1) + ' ' + str(number2) + ' '
        answer = prompt.string(quest, empty=True)
        value = gcd(number1, number2)
        if int(answer) == value:
            correct_answers += 1
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}"'.format(answer, value))
            print('Let\'s try again, {}!'.format(name))
            break

    if correct_answers == 3:
        print('Congratulations, {}!'.format(name))
