from random import randint

from brain_games.brain_engine.const import PRIME_RULES

RULES = PRIME_RULES


def get_ask_question():
    return PRIME_RULES


def is_prime(num):  # проверка на простое число
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generation_number():  # генерация числа
    random_number = randint(1, 10)
    question = str(random_number)
    true_answer = 'yes' if is_prime(random_number) else 'no'
    return true_answer, question