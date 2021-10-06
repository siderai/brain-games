import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
            print('May I have your name? ', end='')
            name = input()
    correct_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers != 3:
        number = random.randint(0, 31231)
        quest = 'Question: ' + str(number) + ' '
        answer = prompt.string(quest, empty=True)
        if (answer == 'yes' and number % 2 == 0) or (answer == 'no' and number % 2 == 1):
            correct_answers += 1
            print('Correct!')
        else:
            if number % 2 == 1:
                antipode = 'no'
            else:
                antipode = 'yes'
            print('"{}" is wrong answer ;(. Correct answer was "{}"'.format(answer, antipode))
            print('Let\'s try again, {}!'.format(name))
            break

    if correct_answers == 3:
        print('Congratulations, {}!'.format(name))
