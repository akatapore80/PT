# Count Occurrences of an Item

# Create a list of fruits with duplicates: ["apple", "banana", "apple", "cherry", "apple"].

# Use a for loop to count how many times "apple" appears.

# Print the count.

fruits = ["apple", "banana", "apple", "cherry", "apple"]

count = 0
for x in fruits :

    if x == "apple" :
        count +=1

print(count)
