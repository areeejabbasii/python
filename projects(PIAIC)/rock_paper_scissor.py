import random
option=("rock","paper","scissor")
running=True
while running:
    player=None
    computer=random.choice(option)
    while player not in option:
        player=input("enter a choice(rock,paper,scissor)")
    print(f"player:{player}")
    print(f"computer:{computer}")
    if player==computer:
        print("its tie")
    elif player=="paper" and computer=="rock":
        print("you win")
    elif player=="rock" and computer=="scissor":
        print("you win")
    elif player=="scissor" and computer=="paper":
        print("you win")
    else:
        print("you lose")
    if not input("playagain?yes/no").lower() =='y':
        running=False
print("thanks for playing")

