# Find the maximum and minimum value in a list without using built-in functions.

listNumber = [12, 34, 12, 2, 32, 23]

max = listNumber[0]
min = listNumber[0]
for num in listNumber : 
    if num > max :
        max = num
    
    if  num < min : 
        min = num

print("max number", max)
print("min number", min)


