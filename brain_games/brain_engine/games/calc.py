from random import choice, randint

from brain_games.brain_engine.const import CALC_QUEST, MATHS_OPERATORS

RULES = CALC_QUEST


def get_ask_question():
    return CALC_QUEST


def get_result_by_math_oper(num1, num2, math_oper):  # вычисление выражений
    if math_oper == '+':
        return num1 + num2
    elif math_oper == '-':
        return num1 - num2
    elif math_oper == '*':
        return num1 * num2
    else:
        raise ValueError(f'Unsupported operator: {math_oper}')


def generation_number():  # Генерация случ. выражения и его правильный ответ
    num1, num2 = randint(1, 10), randint(1, 10)
    math_oper = choice(MATHS_OPERATORS)
    true_answer = get_result_by_math_oper(num1, num2, math_oper)
    question = f'{num1} {math_oper} {num2}'
    return str(true_answer), question
