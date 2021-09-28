a = input("Game 1, W or L ")
b = input("Game 2, W or L ")
c = input("Game 3, W or L ")
d = input("Game 4, W or L ")
e = input("Game 5, W or L ")
f = input("Game 6, W or L ")

if a == "w":
    a = 1
else:
    a = 0

if b == "w":
    b = 1
else:
    b = 0

if c == "w":
    c = 1
else:
    c = 0

if d == "w":
    d = 1
else:
    d = 0

if e == "w":
    e = 1
else:
    e = 0

if f == "w":
    f = 1
else:
    f = 0


if (a + b + c + d + e + f) == 5:
    print("Group 1")
elif (a + b + c + d + e + f) == 6:
    print("Group 1")
elif (a + b + c + d + e + f) == 4:
    print("Group 2")
elif (a + b + c + d + e + f) == 3:
    print("Group 2")
elif (a + b + c + d + e + f) == 2:
    print("Group 1")
elif (a + b + c + d + e + f) == 1:
    print("Group 1")
else:
    print("Eliminated from tournament")
