antena = int(input("How many antenas were on the alien? "))
eye = int(input("How many eyes were on the alien? "))

if antena >= 3 and eye <= 4:
    print("TroyMartian")
elif antena <= 6 and eye >= 2:
    print("VladSaturnian")
elif antena <= 2 and eye <= 3:
    print ("GraemeMercuian")
else:
    print("Your description does not match any of the aliens in our data base")
