import random
def main():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f"die1 is {die1} ")
    print(f"die2 is {die2}")
    print(f"die1 and die2 is {die1+die2}")
for  _ in range(2):
    main()