from random import randint

from brain_games.brain_engine.const import (
    POGRESSION_RULES,
    MAX_PROGRESSION_LENGTH,
    MIN_PROGRESSION_LENGTH, MIN_NUM, MAX_NUM
)

RULES = POGRESSION_RULES


def get_ask_question():
    return POGRESSION_RULES


def generation_number():
    start, step = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
    progr = []
    progr_length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    for i in range(progr_length):
        progr.append(start + step * i)
    missed_index = randint(MIN_NUM, progr_length - 1)
    true_answer = progr[missed_index]
    progr[missed_index] = '..'
    question = ' '.join(map(str, progr))
    return str(true_answer), str(question)
