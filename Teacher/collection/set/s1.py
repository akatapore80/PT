# change value of a to z
#  set is unorder
set1 = {"a", "b", "c"}

convertToList = list(set1)

for i in range(len(convertToList)) : 
  
  if convertToList[i] == "a" : 
     convertToList[i] = "z"

print(set(convertToList))