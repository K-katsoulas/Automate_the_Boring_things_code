# This is a guess the number game.
import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20 . ')

#ask player to ask 6 times

for guessesTaken in range(1,7 ):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low ')

    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break   # This condition is the correct guess!



if guess == secretNumber:
    print('Good Job! You guessed my number in ' + str( guessesTaken ) + ' guesses!')
else:
    print('Nope . The number i was thinking of was ' + str(secretNumber))