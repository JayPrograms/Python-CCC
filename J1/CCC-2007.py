print("Goldilocks eats the porridge out of the 3 bear's bowls. The bowl with the most weight is the bowl of Papa Bear, the bowl with the lightest weight is the bowl of Baby Bear, and the bowl with the weight in between is the bowl of Mama Bear. ")

a = int(input("Choose a number to represent the weight of one of the bowls "))
b = int(input("Choose another number to represent the weight of the other bowl "))
c = int(input("Choose the last number to represent the weight of the last bowl "))

if (a > b) and (a < c) or (a < b) and (a > c):
    print("The weight of Mama bear's bowl is", a)
elif (b > a) and (b < c) or (b < a) and (b > c):
    print("The weight of Mama bear's bowl is", b)
else:
    print("The weight of Mama bear's bowl is", c)
