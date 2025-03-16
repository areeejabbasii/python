print("welcome to our resuturant")
print("pizza:66")
print("pasta:RS70")
print("burger:RS56")
print("salad:RS78")
print("coffe:Rs50")
first=input("enter your first order")
print("your order has been added")
other=input("sdo you want something else")
if (other=="Yes"):
    second=input("enter some thing")
    print("your order has been added")
    print(f"the price to pay is",{first+second})
else:
    print(first)
    #you see the fault here