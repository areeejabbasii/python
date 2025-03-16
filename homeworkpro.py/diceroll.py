import random
def roll_dice():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f"die 1:{die1},die2:{die2}")
for _ in range (3):
 roll_dice()