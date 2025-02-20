from random import randint

import prompt


def greet():#приветствие
    print('Welcome to the Brain Games!')


def welcome_user():#запрос имени
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def answer_message():#вывод правил
    print('Answer "yes" if the number is even, otherwise answer "no".')


def random_num(counter=None):#проверка не/четности
    start=1
    finish=100
    random_number = random.randint(start, finish)
    print(f"Question: {random_number}")
    answer_user = prompt.string('Your answer:')
    if random_number%2==0 and answer_user=='yes':
        print('Correct!')
    elif random_number%2!=0 and answer_user=='no':
        print('Correct!')
    else:
        print(f'{answer_user} is wrong answer ;(. Correct answer was "no".\n Let\'s try again, !')
