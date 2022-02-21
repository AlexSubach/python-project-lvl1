import prompt
import random


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('What is the result of the expression?')


def main():
    count = 0
    while count < 3:
        first_numb = random.randint(1, 10)
        second_numb = random.randint(1, 10)
        procedure = ['+', '-', '*']
        sign = random.choice(procedure)
        question = f'{first_numb} {sign} {second_numb}'
        print(f'Question: {question}')
        answer = int(input('Your answer: '))

        def result():
            if sign == '+':
                return int(first_numb + second_numb)
            elif sign == '-':
                return int(first_numb - second_numb)
            elif sign == '*':
                return int(first_numb * second_numb)
        if result() == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result()}'.")
            print(f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
