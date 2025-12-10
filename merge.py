# Merge two  lists into a single  list and print
list1 = [1,2,3,4]
list2 = [4,5,6,7]
list1.extend(list2)
print(list1)

# Find the union of two lists.
union_list = []
for item in list1 + list2:
    if item not in union_list:
        union_list.append(item)

print(union_list)   
