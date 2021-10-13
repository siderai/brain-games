#!/usr/bin/env python
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, {}!'.format(name))
    # every game has its own question to answer
    print('What number is missing in the progression?')
    # to succeed you have to give 3 right answers in a row
    correct_answers = 0
    while correct_answers < 3:
        # generate variables for creating the task
        start_number = random.randint(0, 30)
        step = random.randint(0, 20)
        missing_index = random.randint(1, 9)
        # create list of progression's elements
        sample_ints = elems_listing(start_number, step)
        sample = [str(x) for x in sample_ints]
        # save correct value then hide it
        value = sample[missing_index]
        sample[missing_index] = '..'
        # convert progression into string with one randomly missing element
        progression_as_string = ' '.join(sample)
        quest = 'Question: ' + progression_as_string + ' '
        answer = prompt.string(quest, empty=True)
        if answer == value:
            # Counting correct answers up to 3
            correct_answers += 1
            print('Correct!')
        else:
            # Wrong answer ends the game
            print('"{}" is wrong answer ;(. '.format(answer),
                  'Correct answer was "{}"'.format(value))
            print('Let\'s try again, {}!'.format(name))
            break
    if correct_answers == 3:
        print('Congratulations, {}!'.format(name))


def elems_listing(start, step):
    progression = [start]
    i = 1
    while i <= 9:
        current = progression[i - 1] + step
        progression.append(current)
        i += 1
    return progression
