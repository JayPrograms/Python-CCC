m = int(input("What are the max hours "))
h = int(input("What is the humidity? "))
t = 1
t += 1
while t <= m:
    a = -6 * (t**4) + h * (t**3) + 2 * (t**2) + t

    if t == m and a > 0:
        print("The ballon does not reach the gound in the given time")
    else:
        print("The balloon reaches the ground in the given time, at hour", t)

    break;

    

