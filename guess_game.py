import random

print(" Number Guessing Game")
print("I am thinking of a number between 1 and 100")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f" Correct! You guessed it in {attempts} attempts.")
        break