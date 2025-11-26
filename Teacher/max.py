# Find the largest of two numbers: Accept two numbers from the user and print the larger one.

def max_funtion(num1, num2) :
     if num1 > num2 :
        print(num1)
     elif num2 > num1 : 
        print(num2)


# max_funtion(20, 30)
# max_funtion(100, 30)

# Maximum of three numbers: Find the largest among three given numbers.

def maximumFunction(num1, num2, num3) :
   # maxim = 0
   # if 5 > maxim
   #   maxim = 5
   # if 4 > maxim
   #    maxim = 4
   # print(maxim)

   maxVal = num1
   if num2 > maxVal :
      maxVal = num2 
   if num3 > maxVal :
      maxVal = num3
   print("The largest number is :", maxVal)


maximumFunction(3,2,30)

