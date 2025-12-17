# 2. Access the third element of a tuple (10, 20, 30, 40, 50).
toplist = (10,20,30,40,50)
print(toplist[2])
# 3. Check if an element exists in a tuple (1, 2, 3, 4, 5). For example, check if 3 is present.
toplist = (1,2,3,4,5)
if 3 in toplist:
    print("Yes present")

# 4. Find the length of a tuple (‘apple’, ‘banana’, ‘cherry’).
toplist = ("apple", "banana","cherry")
print(len(toplist))

# 5. Concatenate two tuples (1, 2, 3) and (4, 5, 6) into a single tuple.
top1 = (1, 2, 3)
top2 = (4, 5, 6) 
top =  top1 + top2
print(top)
# 6. Convert a list to a tuple. Example: [‘red’, ‘green’, ‘blue’].
colors = ['red', 'green', 'blue']
colors_tuple = tuple(colors)
print(colors_tuple)
