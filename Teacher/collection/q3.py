# Count Occurrences of an Item

# Create a list of fruits with duplicates: ["apple", "banana", "apple", "cherry", "apple"].

# Use a for loop to count how many times "apple" appears.

# Print the count.

fruits = ["apple", "banana", "apple", "cherry", "apple", "orange", "orange", "water melon"]


count = 0
for x in fruits :

    if x == "apple" :
        count +=1

print("know occurence is : ", count)

# qsub1 :  Use a for loop to count how many times pass value appears.


def checkOccurence (item) :
    countNum = 0 
    for x in fruits :
        if x == item :
            countNum +=1
    return countNum

data = checkOccurence("orange")

print("unknown occurence is : ", data)