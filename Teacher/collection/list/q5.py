# Reverse a List Using a For Loop

# Create a list of numbers: [1, 2, 3, 4, 5].

# Use a for loop to reverse the list manually (without reverse() or slicing).

# Print the reversed list.

listNumber = [1, 2, 3, 4, 5]

reverseList = []


for num in listNumber :

    reverseList.insert(0, num)

print(reverseList)

# ----------------------------------------------------------------------- 2 solution
reverseListRange = []

for i in range(len(listNumber) - 1, -1, -1) :
    reverseListRange.append(listNumber[i])

print(reverseListRange)


# Range(start, stop, interval)
# len(listNumber) return 5
# Range(len(listNumber) - 1, -1, -1)
#        listNumber[4] 
#  4-1 = listNumber[3]
#  3-1 = listNumber[2]
#  2-1 = listNumber[1]
#  1-1 = listNumber[0]
 