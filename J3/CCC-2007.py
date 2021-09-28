cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
case_money = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
case_total = int(input("What are the total cases? "))
sums = 0

for i in range(case_total):
    cases_left = int(input("What cases have been eleminated? "))
    cases.remove(cases_left)

banker = int(input("What is the banker's offer? "))

for j in range(len(cases)):
    sums += case_money[cases[j]-1]

if sums/len(cases) > banker:
        print('No Deal')

else:
        print('Deal')


    
    
