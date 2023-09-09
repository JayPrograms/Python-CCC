n = int(input())

ans = 0
total = 0
rem = 0

for i in range(n):
    total = i*5
    rem = n-total
    if(rem>=0 and rem %4 == 0):
        ans+=1
print(ans)