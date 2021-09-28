a = int(input("T1 Value "))
b = int(input("T2 Value "))
count = 2
difference = a-b

while difference >= 0:
    count += 1
    c = difference
    difference = b-c
    b = c 

print(count)
    
    
