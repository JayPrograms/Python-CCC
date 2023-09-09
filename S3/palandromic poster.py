import random

def letter():
    letter = chr(random.randint(ord('a'), ord('s')))
    return letter

def letter2():
    letter = chr(random.randint(ord('t'), ord('z')))
    return letter

num = input()
arr = num.split(" ")

n = int(arr[0])
m = int(arr[1])
r = int(arr[2])
c = int(arr[3])

words = [[0]*n]*m

for i in range(n):
    for j in range(m):
        words[i][j] = letter()


x = n/2
print(round(x))

for i in range(n):
    words[i][round(x)] = letter2()


print(words)