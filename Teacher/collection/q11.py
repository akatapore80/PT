# Remove duplicates from a list without using set().

listNumber = [2, 3, 2, 4, 5, 4, 6 ]

reserveList = []

for num in listNumber :
   if num not in reserveList : 
     reserveList.append(num)
     

print(reserveList)
     
    

