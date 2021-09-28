letters = input("As what contact name would you like to save the number? ")
x = []

while letters != "halt":
    x.append(letters)
    letters = input("What other contact name would you like? ")
    
    for letters in range(len(x)):
        presses = 0

        for k in range(len(x[letters])):
            if x[letters][k] in "adgjmptw":
                presses += 1
            elif x[letters][k] in "behknqux":
                presses += 2
            elif x[letters][k] in "cfilorvy":
                presses += 3
            else:
                presses += 4
        
        print(presses)
