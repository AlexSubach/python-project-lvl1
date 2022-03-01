from random import randint, choice


def get_description():
    return 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(0, 20)
    finish = randint(40, 60)
    step = randint(2, 5)
    generate_list = list(range(start, finish, step))
    random = choice(generate_list)
    new_list_0 = str(generate_list).replace(',', '')
    new_list = str(new_list_0).replace(str(random), '..')
    question = f'Question: {new_list.strip("][")}'
    correct_answer = random
    return question, str(correct_answer)
