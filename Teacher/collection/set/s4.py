# Detect Duplicate in Array  
# Use a set to check if an array contains any duplicate elements.

arr = [1,2,3,1,3,4,5]

arr1 = [1,2,3,4,5]

def detectDuplicate (arrData) : 
  mySet = set()
  for num  in arrData : 
    if num in mySet :
       return True
    else :
        mySet.add(num)

  return False


print(detectDuplicate(arr))
print(detectDuplicate(arr1))