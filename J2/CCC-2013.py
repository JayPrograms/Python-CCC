word = input("What is the word? ")

for i in range(len(word)):
    if (i == len(word) - 1) and (word [i] in "ioshzxn"):
        print("Yes")
    else:
        print("No")
    break;
