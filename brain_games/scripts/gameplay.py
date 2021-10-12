#!/usr/bin/env python

def main():
    pass

# function receives a string and a function
def play(question, game):
    # greeting 
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
            print('May I have your name? ', end='')
            name = input()
    print('Hello, {}!'.format(name))
    # every game has its own question to answer
    print(question)
    # to succeed you have to give 3 right answers in a row
    correct_answers = 0
    while correct_answers < 3:
        # every game returns answer and value
        final_pack = game
        answer = final_pack[0]
        value = final_pack[1]
        if check_answer(answer, value) is True:
            # Counting correct answers up to 3
            correct_answers += 1
            print('Correct!')
        else:
            # Wrong answer ends the game
            print('"{}" is wrong answer ;(. Correct answer was "{}"'.format(answer, value))
            print('Let\'s try again, {}!'.format(name))
            break
    
    if correct_answers == 3:
        print('Congratulations, {}!'.format(name))


def check_answer(answer, value):
    if answer == value:
        return True
    else:
        return False
