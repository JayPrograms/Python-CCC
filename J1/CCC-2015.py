m = int(input("What is the month? (use numbers) "))
d = int(input("What is the day? (use umbers) "))

fm = 2
dm = 18

if m < fm:
    print("Before febuary 18")
elif m == fm and d < dm:
        print("Before febuary 18")
elif m > fm:
     print("After febuary 18")
elif m == fm and d > dm:
    print("After febuary 18")
elif m == fm and d == dm:
    print("On febuary 18, special day")
else:
    print("Error")
