# Find pairs with sum k


def findPair(k) : 
    listNumber = [25, 10, 30, 20, 40, 30, 50]
    savePair = []
    for i in range(len(listNumber)) : 
        for index in range(len(listNumber)) :
            if i == index :
                continue
            else : 
                sumItem = listNumber[i] + listNumber[index]
                if sumItem == k :
                    savePair.append(listNumber[i])
                    savePair.append(listNumber[index])
    return set(savePair)


print(findPair(50))
print(findPair(40))
print(findPair(42))