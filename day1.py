#30-days-code-challenge- DAY 1
#learning python basics

#learnt about the various datatypes,operators,string funvtions and several looping stmt.

#using random()
import random
print(random.randrange(1,1000))

#creating a new function
def function():
   print("im on my day one of the CTC 30days code challenge")
function()

#using loops
n = int(input("Enter number: ")) 
if(n == 0 or n < 0):
    print("Value of n be greater than 1")
else:
    fact = 1
    while(n): #while
        fact *= n
        n=n-1
    print(f"Factorial is {fact} ")

#arrays
def sum(arr):
    result = 0
    for x in arr:
        result += x
    return result
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print ('sum_1: {}'.format(sum(arr)))
    


