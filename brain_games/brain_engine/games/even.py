from random import randint
from brain_games.brain_engine.const import MIN_NUM, MAX_NUM

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):  # проверка четности
    return number % 2 == 0


def generation_number():  # генерация числа
    random_number = randint(MIN_NUM, MAX_NUM)
    question = str(random_number)
    true_answer = 'yes' if is_even(random_number) else 'no'
    return true_answer, question
