#30-days-code-challenge- DAY 27(6/7/22)
#learning python basics

nums = []
print("Enter 5 elements for the list: ")
for i in range(5):
    val = int(input())
    nums.append(val)

sum = 0
for i in range(5):
    sum = sum + nums[i]

print("\nSum of all elements =", sum)