a = int(input("What is the degree of the first angle? "))
b = int(input("What is the degree of the second angle? "))
c = int(input("What is the degree of the third angle? "))

if (a + b + c) == 60:
    print("The triangle is an Equilateral")
elif a == c or b == a or c == b and (a + b + c) == 180:
    print("The triangle is an Isosceles")
elif (a + b + c) == 180:
    print("The triangle is Scalene")
else:
    print("error")
