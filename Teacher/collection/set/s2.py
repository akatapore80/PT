# Find pairs with sum k
# Problem: Find Pairs With Sum K
# Description

# You are given an array (or list) of integers and an integer K.
# Your task is to find all unique pairs of numbers in the array whose sum is equal to K.

# A pair consists of two different elements, and each pair should be counted only once, even if the same numbers appear multiple times in the array.


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
                    tuppleValue = tuple(sorted(newList))
                    savePair.add(tuppleValue)
    return savePair




print(findPair(50))
print(findPair(40))
print(findPair(42))