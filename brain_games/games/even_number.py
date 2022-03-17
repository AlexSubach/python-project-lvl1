#!/usr/bin/env python
from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 1000)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
