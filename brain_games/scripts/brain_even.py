import prompt
import random
import brain_games

def main():
    correct_answers = 0
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers != 3:
        number = random.randit()
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
            print('{}'.format(answer) + ' is wrong answer ;(. Correct answer was ' + antipode)
            print('Let\'s try again, {}!'.format(name))
            break

    if correct_answers == 3:
        print('Congratulations, {}!'.format(name))


brain_games.main()
name = welcome_user()
main()
