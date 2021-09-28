print("Press 4 to see the playlist")
button = int(input("Which button do you press? "))
times = int(input("How many times do you press the button? "))
playlist = ["A", "B", "C", "D", "E"]

temp = " "

buttonstring = 0

while button != 4:
    for i in range(times):
        if button == 1:
            temp = playlist [0]
            playlist [0] = playlist [4]
            playlist [4] = temp
        elif button == 2:
            temp = playlist [4]
            playlist [4] = playlist [0]
            playlist [0] = temp
        elif button == 3:
            temp = playlist [0]
            playlist [0] = playlist [1]
            playlist [1] = temp
        else:
            print(playlist)
    break;

a = int(input())

if a == 4:
    print(playlist)
else:
    print("try again")
    

