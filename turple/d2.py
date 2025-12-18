
# 1. Given t = ((1,2,3), (4,5,6), (7,8,9)), write code to access 8.
t = ((1,2,3), (4,5,6), (7,8,9))
print(t[2][1])

# 2. Concatenate two tuples and sort the resulting tuple.
tuple1 = (3, 1, 4)
tuple2 = (2, 5, 6)
tuple = tuple1 + tuple2 
print(tuple)

# 3. Pack multiple values into a tuple, then unpack them into variables.
packed = (10, 20, 30)
a, b, c = packed
print(a, b, c) 


# 4. Show how to “modify” a tuple by converting it to a list and back.
t = (1, 2, 3)
temp_list = list(t)
temp_list[1] = 13
print(temp_list)
modified = tuple(temp_list)

print(modified)  


