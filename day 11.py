#30-days-code-challenge- DAY 11(20/6/22)
#learning python basics


#fibonacci series
a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end=" ")
    n=n-1
