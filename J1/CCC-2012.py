a = int(input("Enter speed limit "))
b = int(input("Enter the recorded speed of the car "))

if b <= a:
    print("Congratulations, you are within the speed limit!")
elif a < b < a + 20:
    print("You are speeding and your fine is $100")
elif a + 21 < b < a + 30:
    print("You are speeding and your fine is $270")
elif b > a + 31:
    print("You are speeding and your fine is $500")
else:
    print("Error: there was an issue please re-run the program")
