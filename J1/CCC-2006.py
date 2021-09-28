print ("welcome to our restaraunt, we have 4 options of burgers. Cheese burger, Veggie burger, Fish burger, and no burger")

burger = int(input("please enter the burger option (1, 2, 3, or 4):" ))
print ("Option ", burger ," okay, we also have drink options" )

print (" we got soft drinks, oranje juice, and milk. You can also choose not to have a drink")
drink = int(input(" please enter the drink option (1, 2, 3, or 4):" ))
print ("option ", drink ," okay we also have sideorder choices" )

print (" we got fries, baked potatoes, chef salad and a no side order option" )
sideorder = int(input(" please enter the sideorder option (1, 2, 3, or 4):" ))
print ("option ", sideorder  ,'okay, for our final options we have dessert choices')

print (" we have apple pie, sundae, fruit cup, and our final option of no dessert")
dessert = int(input(" please insert your desert option (1, 2, 3, or 4):" ))
print ("option ", dessert ,"okay that will be our final option on our menus" )

totalcalorie = 0

if burger == 1:
    totalcalorie = (totalcalorie + 461)
elif burger == 2:
    totalcalorie = (totalcalorie + 431)
elif burger == 3:
    totalcalorie = (totalcalorie + 420)
else:
    totalcalorie = (totalcalorie + 0)


if drink == 1:
    totalcalorie = (totalcalorie + 130)
elif drink == 2:
    totalcalorie = (totalcalorie + 160)
elif drink == 3:
    totalcalorie = (totalcalorie + 118)
else:
    totalcalorie = (totalcalorie + 0)


if sideorder == 1:
    totalcalorie = (totalcalorie + 100)
elif sideorder == 2:
    totalcalorie = (totalcalorie + 57)
elif sideorder == 3:
    totalcalorie = (totalcalorie + 70)
else:
    totalcalorie = (totalcalorie + 0)



if dessert == 1:
    totalcalorie = (totalcalorie + 167)
elif dessert == 2:
    totalcalorie = (totalcalorie + 266)
elif dessert == 3:
    totalcalorie = (totalcalorie + 75)
else:
    totalcalorie = (totalcalorie + 0)

print("your total calorie count for the selected meals are", totalcalorie)


