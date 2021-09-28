lines = int(input("Total lines "))
output = []
output1 = ""
for i in range(lines):
    a = input()
    while a != "":
        C = a[0]
        B = a.count(a[0])
         
        output.extend(B)
        output.append(C)
    
        for j in range(B):
            a = a.replace(C, "")

            output1 = str(output)[1:-1]
            
print(output1)
    
    
    

