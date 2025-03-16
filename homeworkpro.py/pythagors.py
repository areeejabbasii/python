import math
def main():
    base=float(input("enter a base"))
    perp=float(input("enter a perp"))
    hyp=math.sqrt(base**2+perp**2)
    print(f"the hypotenuse is {hyp}")
if __name__ =='__main__':
    main()