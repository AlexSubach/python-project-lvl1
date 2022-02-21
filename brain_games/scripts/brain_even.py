#!/usr/bin/env python
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    def is_even():
        print('Answer "yes" if the number is even, otherwise answer "no".')
        count = 0
        while count < 3:
            random_numb = randint(1, 1000)
            print(f'Question: {random_numb}')
            answer = input('Your answer: ')
            if random_numb % 2 == 0 and answer == 'yes':
                print('Correct!')
                count += 1
            elif random_numb % 2 != 0 and answer == 'no':
                print('Correct!')
                count += 1
            elif random_numb % 2 == 0 and answer == 'no':
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
            elif random_numb % 2 != 0 and answer == 'yes':
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
            if count == 3:
                print(f'Congratulations, {name}!')
                break
            if answer != 'yes' and answer != 'no':
                print(f'Sorry,"{answer}" this is invalid input!')
                break
    is_even()


if __name__ == '__main__':
    main()
