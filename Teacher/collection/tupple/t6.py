# Find the index of the first occurrence of a given element in a tuple

myTupple = (2, 3, 4, 9, 7, 4, 5, 6, 5, 9, 7, 4)

givenNumber = 9

x = myTupple.index(givenNumber)

# print(x)


#  solve without internal function
index = 0
for i in range(len(myTupple)) :
    if myTupple[i] == givenNumber :
          index = i
          break

print(index)