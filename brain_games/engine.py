import prompt


GAME_ROUND = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.description)
    for _ in range(GAME_ROUND):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")   # noqa: E501
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
