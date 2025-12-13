# 1.Create a list and insert elements at the beginning, middle, and end.

listNumber = [1, 2, 3, 4, 5]

listNumber.insert(0, 6)
print(listNumber)


middle = len(listNumber) // 2

listNumber.insert(middle, 10)
print(listNumber)

# end = len(listNumber)
# listNumber.insert(end, 20)

listNumber.append(20)
print(listNumber)
