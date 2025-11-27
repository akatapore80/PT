# Check Multiples

# Ask the user to input two numbers.

# Use a conditional to check if the first number is a multiple of the second.

# Print "Yes" if true, otherwise "No
num1 = input("Enter first number")
num2 = input("Enter second number")
num1 = int(num1)
num2 = int(num2)

def myMultiple(num1,num2):
    if num1 % num2 == 0:
        print("Yes")
    else:
        print("No")
myMultiple(num1,num2)