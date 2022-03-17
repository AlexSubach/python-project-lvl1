#!/usr/bin/env python
from random import randint, choice
from operator import add, mul, sub


description = 'What is the result of the expression?'


def get_question_and_answer():
    first_numb = randint(1, 10)
    second_numb = randint(1, 10)
    operations = [('+', add), ('-', sub), ('*', mul)]
    (operator, func_operator) = choice(operations)
    question = f'{first_numb} {operator} {second_numb}'
    correct_answer = (func_operator)(first_numb, second_numb)
    return question, str(correct_answer)
