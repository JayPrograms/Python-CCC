l = int(input("Total lines "))
i = 0
x = []
output = 0

while i < l:
    a = input("what is the message? ")
    b = a.split()
    for c in a:
        x.append(c)

    i += 1

for i in range(0, len(x), 2):
    line = int(x[i]) * int(x[i+1])
    print(line)

        
