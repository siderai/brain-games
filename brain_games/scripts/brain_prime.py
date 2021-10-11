import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
            print('May I have your name? ', end='')
            name = input()
    print('Hello, {}!'.format(name))
    correct_answers = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while correct_answers < 3:
        number = random.randint(0, 37)
        quest = 'Question: ' + str(number) + ' '
        answer = prompt.string(quest, empty=True)
        if answer == is_prime(number):
            correct_answers += 1
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}"'.format(answer, is_prime(number)))
            print('Let\'s try again, {}!'.format(name))
            break
    if correct_answers == 3:
        print('Congratulations, {}!'.format(name))


def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return 'no'
            else:
                return 'yes'
    else:
        return 'no'
