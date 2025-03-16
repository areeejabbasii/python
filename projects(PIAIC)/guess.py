
import random

random_number = random.randint(1, 100)
tries = 0

while True:
    try:
        guess = int(input("Enter a number: "))
        tries += 1

        if guess == random_number:
            print(f"You guessed it in {tries} tries!")
            break
        elif guess > random_number:
            print("You guessed too high.")
        elif guess < random_number:
            print("You guessed too low.")
    except ValueError:
        print("Invalid input! Please enter a number.")
