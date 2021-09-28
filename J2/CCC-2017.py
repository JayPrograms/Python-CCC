n = int(input("What is the starting number? "))
k = int(input("How many times does it get shifted? "))
sums = 0

if k == 0:
    sums = n
elif k == 1:
    sums = n + (n * 10)
elif k == 2:
    sums = n + (n * 10) + (n * 100)
elif k == 3:
    sums == n + (n * 10) + (n * 100) + (n * 1000)
elif k == 4:
    sums == n + (n * 10) + (n * 100) + (n * 1000) + (n * 10000)
elif k == 5:
    sums == n + (n * 10) + (n * 100) + (n * 1000) + (n * 10000) + (n * 100000)
else:
    print("Re-run program")

print(sums)
