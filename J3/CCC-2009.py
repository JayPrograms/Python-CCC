Ottawa = int(input("Ottawa time "))
print(Ottawa, "In Ottawa")

Victoria = Ottawa - 300
if Victoria < 0:
    Victoria = 2400 + Victoria
    print(Victoria, "In Victoria")
else:
    Victoria = Ottawa - 300
    print(Victoria, "In Victoria")

Edmonton = Ottawa - 200
if Edmonton < 0:
    Edmonton = 2400 + Edmonton
    print(Edmonton, "In Edmonton")
else:
    Edmonton = Ottawa - 200
    print(Edmonton, "In Edmonton")

Winnipeg = Ottawa - 100
if Winnipeg < 0:
    Winnipeg = 2400 + Winnipeg
    print(Winnipeg, "In Winnipeg")
else:
    Winnipeg = Ottawa - 100
    print(Winnipeg, "In Winnipeg")

print(Ottawa, "In Toronto")

Halifax = Ottawa + 100
if Halifax > 2400:
    Halifax = 0 + Halifax
    print(Halifax, "In Halifax")
else:
    Halifax = Ottawa + 100
    print(Halifax, "In Halifax")

John = Ottawa + 130
if John > 2400:
    John = 0 + John
    print(John, "In St. John's")
else:
    John = Ottawa + 130
    print(John, "In St. John's")
