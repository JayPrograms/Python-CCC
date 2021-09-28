a = int(input("First reading "))
b = int(input("Second reading "))
c = int(input("Third reading "))
d = int(input("Last reading "))
list = []

list.append (a)
list.append (b)
list.append (c)
list.append (d)

if list [0] > list [1] > list [2] > list [3]:
    print("Fish diving")
elif list [0] < list [1] < list [2] < list [3]:
    print("Fish rising")
elif list [0] == list [1] == list [2] == list [3]:
    print("Fish is in constant depth")
else:
    print("No fish")
