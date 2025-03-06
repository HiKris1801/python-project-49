from random import randint

from brain_games.brain_engine.const import (
    MAX_NUM,
    MAX_PROGRESSION_LENGTH,
    MIN_NUM,
    MIN_PROGRESSION_LENGTH,
    POGRESSION_RULES,
)

RULES = POGRESSION_RULES


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
