import math
from random import randint

from brain_games.brain_engine.const import GCD_ACTION, MAX_NUM, MIN_NUM

RULES = GCD_ACTION


def get_ask_question():
    return GCD_ACTION


def generation_number():  # Генерация случайных чисел и его правильный ответ
    num1, num2 = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
    true_answer = math.gcd(num1, num2)
    question = f'{num1} {num2}'
    return str(true_answer), question
