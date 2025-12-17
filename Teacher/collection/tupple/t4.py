# Given a tuple of integers, find the maximum and minimum elements.

myTupple = (4, 5, 45, 345, 2, 1, 3, 2, -10)

max = myTupple[0]
min = myTupple[0]
for num in myTupple : 

    if num > max : 
        max = num
    if num < min :
        min = num


print("my max", max)
print("my min", min)