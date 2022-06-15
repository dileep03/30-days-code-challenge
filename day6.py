#30-days-code-challenge- DAY 6(15/6/22)
#learning python basics

#linear search

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

arr = [ 1,3,2,5,7 ]
result=search(arr,5) 
print("the required element is at index",result)
