import prompt
from random import randint


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('Find the greatest common divisor of given numbers.')


def main():
    count = 0
    while count < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f'Question: {a} {b}')
        answer = int(input('Your answer: '))
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        c = a + b
        if c == answer:
            print('Correct!')
            count += 1
        elif c != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{c}'.")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
