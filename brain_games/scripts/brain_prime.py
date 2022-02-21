import prompt
from random import randint


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('Answer "yes" if given number is prime. Otherwise answer "no".')


def main():
    count = 0
    while count < 3:
        number = randint(2, 500)

        def is_prime(number):
            if number == 2 or number == 3:
                return True
            if number % 2 == 0 or number < 2:
                return False
            for i in range(3, int(number ** 0.5) + 1, 2):
                if number % i == 0:
                    return False
            return True

        print(f'Question: {number}')
        answer = input('Your answer: ')
        if is_prime(number) is True and answer == 'yes':
            print('Correct!')
            count += 1
        if is_prime(number) is False and answer == 'yes':
            print(f"'yes' it is don't correct, correct answer is 'no'")
            break
        if is_prime(number) is False and answer == 'no':
            print('Correct!')
            count += 1
        if is_prime(number) is True and answer == 'no':
            print(f"'no' it is don't correct, correct answer is 'yes'")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()
