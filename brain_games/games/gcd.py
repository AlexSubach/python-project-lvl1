from random import randint
from math import gcd


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = f'Question: {first_number} {second_number}'
    correct_answer = gcd(first_number, second_number)
    return question, str(correct_answer)
