# Count how many times each element appears in a tuple

# create two list one for value and for count
# for value list we check if the value exist so that we can skip this value or duplicate count
#  we can skip loop by continue keyword

myTupple = (2, 3, 2, 4, 5, 6, 2, 3, 4, 4, 4, 1, 1, 1)

listValue = []
listOccurence = []
 
#  2  2
#  2 3
#  2 4
#  2 5
#  2 6
#  2 2


count = 0
for num in myTupple : 

    if num in listValue : 
        continue

    for x in myTupple : 
        if num == x : 
            count +=1

    if count > 0 : 
        listValue.append(num)  
        listOccurence.append(count) 

    count = 0

print(tuple(listValue))   
print(tuple(listOccurence))     

   