import random

print("------ NUMBER GUESSING GAME ------")

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret:
        print("Too Low! Try again.")

    elif guess > secret:
        print("Too High! Try again.")

    else:
        print("Correct! You guessed the number.")

