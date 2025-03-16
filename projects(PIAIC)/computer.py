
import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0


    while guess != random_number:

        guess = int(input(f"Enter a number between 1 and {x}: "))

        if guess > random_number:
            print("Sorry! Guess again, too high try again.")
        elif guess < random_number:
            print("Sorry! Guess is too low  in , try again.")


    print(f"Yay, congrats! You guessed the number {random_number}.")
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !='c':
        guess=random.randint(low,high)
        feedback=input(f'is {guess}too high (H),too loW(L)or correct(C)?')
        if feedback =='h':
            high=guess-1
        elif feedback =='l':
            low=guess+1
    print(f"computer guess your number{guess} correctly")
guess(10)
