a = int(input("3 points scored by apple "))
b = int(input("2 points scored by apple "))
c = int(input("1 points scored by apple "))
d = int(input("3 points scored by banana "))
e = int(input("2 points scored by banana "))
f = int(input("1 points scored by banana "))

sum1 = 0
sum2 = 0

sum1 = (a * 3) + (b * 2) + (c * 1)
sum2 = (d * 3) + (e * 2) + (f * 1)

if sum1 > sum2:
    print("Apple is the winner!")
else:
    print("Banana is the winner!")

