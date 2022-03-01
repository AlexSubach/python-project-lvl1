from random import randint


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 300)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
