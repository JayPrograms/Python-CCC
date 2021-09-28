votes = int(input("What are the total amount of votes? "))
a_votes = 0
b_votes = 0
order = 0

for i in range(votes):
    order = input("What is the vote? ")
    if order == 'A' or 'a':
        a_votes += 1
    elif order == 'B' or 'b':
        b_votes += 1
    else:
        print("Error")

if a_votes > b_votes:
    print("A")
elif b_votes > a_votes:
    print("B")
elif b_votes == a_votes:
    print("tie")
else:
    print("Error")

    
    
    



    
