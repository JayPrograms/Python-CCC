a = int(input("How many steps did Nikky walk forward? "))
b = int(input("How many steps did Nikky walk backward? "))
c = int(input("How many steps did Byron walk forward? "))
d = int(input("How many steps did Byrom walk backward? "))
s = int(input("What are the total steps? "))

ndistance = 0
bdistance = 0

# These are for nikky
nstep = a + b
ndif = a - b
nrem = s % nstep
nd = s // nstep
ndistance = ndistance + (nd * ndif)

# These are for Byrom
bstep = c + d
bdif = c - d
brem = s % bstep
bd = s // bstep
bdistance = bdistance + (bd * bdif)

if nrem <= a:
    ndistance += nrem
elif nrem > a:
    ndistance += a + (nrem - a) * (-b)

if brem <= c:
    bdistance += brem
elif nrem > c:
    bdistance += c + (brem - c) * (-d)


if ndistance > bdistance:
    print("Nikky is further ahead")
elif ndistance < bdistance:
    print("Byrom is further ahead")
else:
    print("They are tied")
