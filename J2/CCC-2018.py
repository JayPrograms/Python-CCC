spaces = int(input("How many spaces? "))
today = input("What is today's information? ")
yesterday = input("What was yesterday's information? ")
same = 0

for i in range(0, int(spaces)):
    if yesterday[i] == today[i] and today[i] == "c":
        same = same + 1

print(same)
