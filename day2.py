#30-days-code-challenge- DAY 1
#learning python basics

#reversing an array
a=[]
n=int(input("enter the no of elements:"))
for i in range(0,n):
    l=int(input())
    a.append(l)

print("the array is :",a)
a.reverse()
print("the reversed array is",a)

#largest no in an array
a=[]
n=int(input("enter the no of elements:"))
for i in range(0,n):
    l=int(input())
    a.append(l)
max=a[0]
for i in range(0,n):
    if a[i]>max:
         max=a[i]
print("the largest number is",max)

