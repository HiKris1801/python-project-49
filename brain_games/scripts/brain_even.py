from random import randint

import prompt


def rules():#вывод правил
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):#проверка четности
    return number%2==0

def generation_number():#генерация числа
    random_number = random.randint(1, 100)
    print(f"Question: {random_number}")
    true_answer= 'yes' if is_even(random_number) else 'no'
    answer_user = prompt.string('Your answer:')
    return true_answer, answer_user
    
def run_game_and_counter_answer():#игра и подсчет правильных ответов
    correct_answer=0
    for _ in range(3):
        true_answer, answer_user = generation_number() # Сохраняем результат вызова generation_number()
        if answer_user.lower()== true_answer:#проверяем правильность ответа
            correct_answer+=1
            print('Correct!')
        else:
            print(f'{answer_user} is wrong answer ;(. Correct answer was {true_answer}.\n Let\'s try again, !')
            return
    if correct_answer==3:# Проверка, сколько правильных ответов было у игрока
        print(f'Congratulations, {name} !')


