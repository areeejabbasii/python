
menu={
    "pizza":56,
     "pasta":67,
     "salt":45,
     "coffee":55,
     "burger":89,
}
print("welecome to python resto")
print("pizza:rs56/npasta:rs67/nsalt:rs45/ncoffee:rs55/nburger:rs89")
ordertotal=0
first=input("enter the item")
if first in menu:
    ordertotal+=menu[first]
    print(f"your item is {first} has been added")
else:
    print(f"order item {first} is not valid")
item=input("do you want second item?yes/no")
if item=="Yes":
  item2=input("enter your other item")
  if item in menu:
    ordertotal+=menu[second]
    print(f"item{item2} has been added")
  else:
    print(f"order item is not avalisble")
print(f"the total amount to pay is {ordertotal}")