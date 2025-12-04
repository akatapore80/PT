# Search for an element in a list (linear search)

myList = ["apple", "banana", "orange", "water melon"]


searchItem = input("Enter the element : ")

if searchItem in myList :
    print(searchItem)
else :
    print("item not found")