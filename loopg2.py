#  print duplicates element from a list.
list = [1,2,3,3,4,5,1,1,6,7]
duplicates = []
for x in list:
    if list.count(x) > 1 and x not in duplicates:
        duplicates.append(x)
print(duplicates)

#  Split a list into two halves
list = [1,2,3,3,4,5,1,1,6,7]

first_half = []
second_half = []
half = len(list) // 2
for x in  range(len(list)):
    if x < half:
        first_half.append(list[x])
    else:
        second_half.append(list[x])
print(first_half)
print(second_half)



