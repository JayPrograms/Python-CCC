weight = float(input("What is your weight in kilograms? "))
height = float(input("What is your height in meters? "))

BMI = weight / (height ** 2)

if (BMI > 25):
    print("You are overweight")
elif (BMI < 18.5):
    print("You are underweight")
else:
    print("You are normal weight")



