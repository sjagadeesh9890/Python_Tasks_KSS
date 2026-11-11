#  Create a Number Guessing Game where: 
'''● The program generates a random number between 1 and 50 using random. 
   ● The user has 5 attempts to guess the number. 
   ● After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.'''
from random import*
from math import*
secret_number = randint(1,50)
print('Welcome to the Number Guessing Game! \nGuess the number between 1 and 50 \nYou have 5 attempts.')
for i in range(1,6):
    guess = int(input(f'Attempt {i}: Enter your guess:-'))
    difference_number = fabs(secret_number - guess)

    if guess == secret_number:
        print('Wow! You guessed the correct number.')
        break
    else:
        print('Wrong number you guessed,\nThe difference away from the correct number is:-',difference_number)

if guess != secret_number:
    print('game Over! \n The correct number is:-',secret_number)
