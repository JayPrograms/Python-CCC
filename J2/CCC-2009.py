trout = int(input("what are the points for the trout "))
pike = int(input("What are the points for the pike "))
pickerel = int(input("What are the points for the pickerel "))
total = int(input("What are the total points allowed for fishing "))
fish = [0]
i = 0
j = 0
k = 0
l = 0

totaltrout = total//trout
totalpike = total//pike
totalpickerel = total//pickerel

for i in range(0 , totaltrout + 1):
    for j in range(0 , totalpike + 1):
        for k in range(0 , totalpickerel + 1):
            if trout + pike + pickerel <= total:
                fish.append([i, j, k])

for i in range(1, len (fish)):
    print(fish[0], "Trout,", fish[1], "Pike, and", fish[2], "Pickerel.")
    print("The number of ways to catch the fish is:", len(fish)-1)
            

