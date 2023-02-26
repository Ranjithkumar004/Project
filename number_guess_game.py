#import libraries
import random

#welcome message
print("Welcome to the number guessing game!\n")

#set/generate random number
number = random.randint(1,20)

#game loop
for i in range(3):
    #prompt user
    guess = int(input("Please guess a number between 1 and 20: "))

    #evaluate guess
    if guess == number:
        print("\nCongratulations! You guessed the correct number!\n")
        break
    elif guess > number:
        print("\nYour guess is too high, please try again.\n")
    else:
        print("\nYour guess is too low, please try again.\n")

#lost message
if guess != number:
    print("Sorry, you lose. The correct number was: ", number)