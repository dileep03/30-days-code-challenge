#30-days-code-challenge- DAY 21(30/6/22)
#learning python basics

#flyod's triangle
rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()
