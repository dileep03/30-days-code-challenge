#30-days-code-challenge- DAY 22(1/7/22)
#learning python basics

#sort words in alphabetical order
print("Enter the String: ")
str = input()

wrds = str.split()
wrds.sort()

sortedwrds = ""
for wrd in wrds:
    sortedwrds = sortedwrds + wrd + " "

print(sortedwrds)