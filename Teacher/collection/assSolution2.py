#  Find the middle element of a list

listNumber=[1,2,3,4,5, 6, 7]

length = len(listNumber)
middleIndex = length // 2
evenElement = middleIndex - 1

if length % 2 == 0 : 
  middleElement =   (listNumber[evenElement] + listNumber[middleIndex]) / 2
  print("my middle number is even  : ", middleElement)
else : 
   middleElement = listNumber[middleIndex]
   print("my middle number is odd  : ", middleElement)

