
import random

def guess():
    input("Press Enter to generate 10 random numbers...")  
    numbers = random.sample(range(1, 101), 10)  
    print("Random numbers:", numbers)

guess()
