# Write a function to reverse a tuple without using slicing.

myTupple = (2,3,3,46,6,4,1)
listNumber = []

for num in myTupple :
    listNumber.insert(0, num)

reverseTupple = tuple(listNumber)
print(reverseTupple)
