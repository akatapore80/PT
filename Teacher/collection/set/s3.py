# #1. Find Union of Two Sets  
# Write a function that takes two sets and returns their union.
set1 = {1,2,3,4}
set2 = {2,4,17,20,17}
set3 = set1.union(set2)
print(set3)


# 2. Find Intersection of Two Sets 
# Implement a function to return the common elements between two sets.
set4 = set1.intersection(set2)
print(set4)


# 3. Find Difference of Two Sets  
# Given two sets, return the elements present in the first but not in the second.
set5 = set1.difference(set2)
print(set5)


# 4. Check Subset  
# Write code to check if one set is a subset of another.
set7 = {1,2,3,3,5,7}
set8 = {1,7,3}
set9 = set8.issubset(set7)
print(set9)

# 5. Remove Duplicates from a List using Set  
# Given a list of integers, remove duplicates efficiently using a set.
list1 = [1,2,3,20,3,3,4]
list2 = set(list1)
print(list2)