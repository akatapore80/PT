
#  Check Even or Odd

# Ask the user to input a number.

# Use a conditional to check if the number is even or odd.

# Print the result.
number = input("enter number")
number = int(number)
def checkEven(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
checkEven(number)

