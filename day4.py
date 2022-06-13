#30-days-code-challenge- DAY 4(13/6/22)
#learning python basics

#checking for a palindrome
def isPalindrome(s):
    return s == s[::-1]

s = input("enter the word:")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


#merging dictionaries
def Merge(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {   'a': 10,   'b': 8}
dict2 = {   'd': 6,    'c': 4}
print(Merge(dict1, dict2))
print(dict2)

