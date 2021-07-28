import random

random_number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))
if guess == random_number:
    print("You guessed it right")
else:
    print("try again")