#  Find the most frequent element in a list

# if is in the list increase the count


listNumber = [1,2,3,3,4,4,4,5,6]

count = 0
mode = 0
# 1,1
# 1,2
# 1,3
# 1,3
# 1,4
# 1,4
# 1,4

# 2,1
# 2,2
# 2,3
# 2,3
# 2,4
# 2,4
# 2,4

# 3,1
# 3,2
# 3,3
# 3,3
# 3,4
# 3,4
# 3,4

# 3,1
# 3,2
# 3,3
# 3,3
# 3,4
# 3,4
# 3,4

# 4,1
# 4,2
# 4,3
# 4,3
# 4,4
# 4,4
# 4,4

# 4,1
# 4,2
# 4,3
# 4,3
# 4,4
# 4,4
# 4,4

# 4,1
# 4,2
# 4,3
# 4,3
# 4,4
# 4,4
# 4,4

# 5,1
# 5,2
# 5,3
# 5,3
# 5,4
# 5,4
# 5,4




occurenceList = []
modeList  = []

for num in listNumber :

    for num1 in listNumber :
        if num == num1 : 
            count +=1
    if count > 1 :
            if count not in occurenceList :
              occurenceList.append(count) 
            if num not in modeList :
               modeList.append(num)   
    count = 0


print(occurenceList)
print(modeList)

max = 0
for num in occurenceList :
    if num > max : 
        max = num


myIndex = occurenceList.index(max)

print("My frequency or occurence is : ", occurenceList[myIndex])
print("My mode element or frequency element is : ", modeList[myIndex])