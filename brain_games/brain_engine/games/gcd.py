from random import randint
import math
from brain_games.brain_engine.const import GCD_ACTION

RULES = GCD_ACTION

def get_ask_question():
    return GCD_ACTION


def generation_number():  # Генерация случайных чисел и его правильный ответ
    num1, num2 = randint(1, 10), randint(1, 10)
    true_answer = math.gcd(num1, num2)
    question = f'{num1} {num2}'
    return str(true_answer), question