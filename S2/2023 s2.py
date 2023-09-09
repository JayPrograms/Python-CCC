x = int(input())
y = list(map(int, input().split()))
for z in range(1, x+1):
    min_asym_val = float('inf')
    for i in range(x - z + 1):
        l = i
        r = i + z - 1
        asym_val = 0
        for j in range((r-l+1)//2):
            asym_val += abs(y[l+j] - y[r-j])
        min_asym_val = min(min_asym_val, asym_val)
    print(min_asym_val, end=' ')
