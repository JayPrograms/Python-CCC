n = int(input())
x = input()
y = input()
line1 = x.split(" ")
line2arr = y. split(" ")
output = int(0)
sidebyside = 0

for i in range(n):
	if int(line1[i]) == int(1):
		if i+1 < len(line1) and int(line1[i+1]) == int(1):
			sidebyside += 1
		elif sidebyside > 0:
			sidebyside +=1
			output += (sidebyside*3) - (sidebyside - 1) * 2
			sidebyside = 0
		else:
			output += 3			
print(output)