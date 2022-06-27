#30-days-code-challenge- DAY 18(27/6/22)
#learning python basics

#count repeated characters in a string
rChar = 0
rCharList = []
k = 0

print("Enter the String: ")
text = str(input())

textList = list(text)
tot = len(text)

for i in range(tot):
  if text[i] in textList:
    if text[i] not in rCharList:
      newText = text[i+1:]
      newTot = len(newText)
      for j in range(newTot):
        if newText[j]==text[i]:
          rChar = rChar+1
          rCharList.insert(k, text[i])
          k = k+1
          break

print("\nTotal Repeated Character(s): ")
print(rChar)
