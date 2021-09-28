drops= int(input("Total drops of paint"))
x = []
y = []
c = 0
d = 0
e = 0
f = 0
for i in range(drops):
    a = int(input("X cord "))
    x.append(a)
    b = int(input("Y cords "))
    y.append(b)

print(x)
print(y)

    
c = (min(x))
c-1
d = (min(y))
d-1

e = (max(x))
e+1
f = (max(y))
f+1

print(c, d)
print(e, f)
