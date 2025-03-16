import random

def guess():
    secret_num = random.randint(1, 99)  # Generate a secret number
    print("I am thinking of a number between 1 and 99.")

    while True:  
        if guess > secret_num:
            print("Oh no! Too high.")
        elif guess < secret_num:
            print("Too low.")
        else:
            print("Congrats! You won 🎉")
            break  
guess()
