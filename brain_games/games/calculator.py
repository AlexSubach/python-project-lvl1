#!/usr/bin/env python
from random import randint, choice
from operator import add, mul, sub


def get_description():
    return 'What is the result of the expression?'


def get_question_and_answer():
    first_numb = randint(1, 10)
    second_numb = randint(1, 10)
    operation = (('+', add), ('-', sub), ('*', mul))
    random_operation = choice(operation)
    question = f'{first_numb} {random_operation[0]} {second_numb}'
    correct_answer = random_operation[1](first_numb, second_numb)
    return question, str(correct_answer)
