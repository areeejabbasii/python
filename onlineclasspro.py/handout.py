
import random
num_rounds=5
score=0
print("welcome to high low game")
print("-"*100)
for round_number in range(1,num_rounds+1):
 print("-"*100)
 print(f"round{round_number}")
 opponent=random.randint(1,100)
 user=random.randint(1,100)
 print(f"your number is{user}")
 user_guess=input("do you think your number is higher or lower")
 if (user_guess=="higher" and user<opponent) or (user_guess=="lower" and user>opponent) :
    print("you got a point +1,the computer number is{opponent}")
    score+=1
 else:
    print(f"wrong anser,the computer number is {opponent}")
print(f"your final score is :{score}")
