# Sum of Numbers in a List

# Ask the user to input numbers into a list (e.g., [2, 4, 6, 8]).

# Use a for loop to calculate the sum of all numbers.

# Print the result.
 
num = input("Enter number")
list_of_digits = []

for x in num : 
    castNum = int(x)
    list_of_digits.append(castNum)


# =================

sum = 0
for data in list_of_digits : 
     sum += data

print(sum)
