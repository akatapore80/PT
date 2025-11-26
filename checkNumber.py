
# get user input of two number , check if both number is positive and print out the multiplication of the number
num1 = input("Enter a number")
num2 = input("Enter a number ")
num1 = int(num1)
num2 = int(num2)

def numbers(num1,num2):

    if num1 > 0 and num2 > 0:
     print(num1 *num2)
numbers(num1,num2)