from random import randint

from brain_games.brain_engine.const import (
    MAX_PROGRESSION_LENGTH,
    MIN_PROGRESSION_LENGTH,
    POGRESSION_RULES,
)

RULES = POGRESSION_RULES


def get_ask_question():
    return POGRESSION_RULES


def generation_number():
    start, step = randint(1, 10), randint(1, 10)
    progr = []
    progr_length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    for i in range(progr_length):
        progr.append(start + step * i)
    missed_index = randint(0, progr_length - 1)
    true_answer = progr[missed_index]
    progr[missed_index] = '..'
    question = ' '.join(map(str, progr))
    return str(true_answer), str(question)
