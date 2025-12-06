# Move all zeros in a list to the end while keeping order.

listNumber = [1,0,2,0,2,3,0,0]
listOfZero = []
listOfNonZero = []

for num in listNumber :
    if num == 0 : 
        listOfZero.append(num)
    else :
        listOfNonZero.append(num)

listOfNonZero.extend(listOfZero)

print(listOfNonZero)