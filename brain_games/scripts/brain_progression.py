import prompt
from random import randint, choice


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('What number is missing in the progression?')


def main():
    count = 0
    while count < 3:
        start = randint(0, 20)
        finish = randint(40, 60)
        step = randint(2, 5)
        generate_list = list(range(start, finish, step))
        rand = choice(generate_list)
        new_list_0 = str(generate_list).replace(',', '')
        new_list = str(new_list_0).replace(str(rand), '..')
        print(f'Question: {new_list.strip("][")}')
        answer = int(input('Your answer: '))
        if answer == rand:
            print('Correct!')
            count += 1
        elif answer != rand:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{rand}'.")
            print(f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
