from random import randint, choice


def get_description():
    return 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(0, 20)
    finish = randint(40, 60)
    step = randint(2, 5)
    generate_list = list(range(start, finish, step))
    random = str(choice(generate_list))
    new_list = str(generate_list).replace(',', '')
    question = f"{new_list.replace(random, '..').strip('][')}"
    correct_answer = random
    return question, str(correct_answer)