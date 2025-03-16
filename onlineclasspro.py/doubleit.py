def double_until_100():
    num = int(input("Enter a number: "))  # Take user input

    while num < 100:  # Repeat until num reaches 100 or more
        num *= 2  # Double the number
        print("Doubled number:", num)  # Print the result

    print("The number has reached 100 or more. Exiting...")  

double_until_100()
