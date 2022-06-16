#30-days-code-challenge- DAY 7(16/6/22)
#learning python basics

#bubble sort

def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return
arr = [64,34,25,100,1,3,12,22,11,90,45,32]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
