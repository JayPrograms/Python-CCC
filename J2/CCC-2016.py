magic1 = []
magic2 = []
magic3 = []
magic4 = []

a = input('What are the first 4 numbers? ')
b = input("What are the second 4 numbers? ")
c = input("What are the next 4 numbers? ")
d = input("What are the last 4 numbers? ")

e = a.split()
f = b.split()
g = c.split()
h = d.split()

magic1.append (e)
magic2.append (f)
magic3.append (g)
magic4.append (h)

i = int(magic1[0][0]) + int(magic1[0][1]) + int(magic1[0][2]) + int(magic1[0][3])
j = int(magic2[0][0]) + int(magic2[0][1]) + int(magic2[0][2]) + int(magic2[0][3])
k = int(magic3[0][0]) + int(magic3[0][1]) + int(magic3[0][2]) + int(magic3[0][3])
l = int(magic4[0][0]) + int(magic4[0][1]) + int(magic4[0][2]) + int(magic4[0][3])

m = int(magic1[0][0]) + int(magic2[0][0]) + int(magic3[0][0]) + int(magic4[0][0])
n = int(magic1[0][1]) + int(magic2[0][1]) + int(magic3[0][1]) + int(magic4[0][1])
o = int(magic1[0][2]) + int(magic2[0][2]) + int(magic3[0][2]) + int(magic4[0][2])
p = int(magic1[0][3]) + int(magic2[0][3]) + int(magic3[0][3]) + int(magic4[0][3])

if i == j == k == l == m == n == o == p:
    print("Magic")
else:
    print("Not Magic")
