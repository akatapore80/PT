# Find pairs with sum k


def findPair(k) : 
    listNumber = [25, 10, 30, 20, 40, 30, 50]
    savePair = set()
    for i in range(len(listNumber)) : 
        for x in range(len(listNumber)) :
            if i == x :
                continue
            else : 
                sumItem = listNumber[i] + listNumber[x]
                if sumItem == k :
                    newList = (listNumber[i], listNumber[x])
                    savePair.add(tuple(sorted(newList)))
    return savePair


print(findPair(50))
print(findPair(40))
print(findPair(42))