# Find Missing Number in Array  
# Given an array of numbers from 1 to n with one missing, use a set to find the missing number.


arr = [1, 2, 4, 5]
arr1 = []

for i in range(len(arr) + 1) :
   arr1.append(i + 1)

convertArr = set(arr)
convertArr1 = set(arr1)

missingNum = convertArr1.difference(convertArr)

print(missingNum)