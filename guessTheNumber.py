#This is a guess a number game program
import random

secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask user to guess the number 6 times
for guessTaken in range (1,7):
    print('Take a guess')
    guess = int(input())

    if guess > secret_number:
        print('Your Guess is too high!')
    elif guess < secret_number:
        print('Your Guess is too low!')
    else:
        break # the user guessed the number correctly

if guess == secret_number:
    print('Good Job , you have guessed my number in ' + str(guessTaken)+ ' guesses!!')
else:
    print('Nope, the number I was thinking was ' + str(secret_number) + '.')

