from random import randint
from brain_games.brain_engine.const import GCD_ACTION, MIN_PROGRESSION_LENGTH,MAX_PROGRESSION_LENGTH
RULES = GCD_ACTION


def get_ask_question():
    return GCD_ACTION

def generation_number():
    start, step = randint(1, 10), randint(1, 10)
    progr=[]
    progr_length=randint(MIN_PROGRESSION_LENGTH,MAX_PROGRESSION_LENGTH)
    for i in range(progr_length):
        progr.append(start+step*i)
    missed_index=randint(0,progr_length-1)
    true_answer=progr[missed_index]
    progr[missed_index]='..'
    question=' '.join(map(str,progr))
    return str(true_answer), str(question)