#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.gameplay import play, check_answer


def main():
    play(question, game())
    
question = 'What number is missing in the progression?'
# написать декоратор который бы заворачивал game() так, чтобы
# функции вызывались в нужном порядке
def the_game():
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
    return answer, value
        

def elems_listing(start, step):
    progression = [start]
    i = 1
    while i <= 9:
        current = progression[i - 1] + step
        progression.append(current)
        i += 1
    return progression
