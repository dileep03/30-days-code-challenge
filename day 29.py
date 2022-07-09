#30-days-code-challenge- DAY 29(8/7/22)
#learning python basics

# Swap function
def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print("before swapping:",List)
print("after swapping:",swapPositions(List, pos1-1, pos2-1))
