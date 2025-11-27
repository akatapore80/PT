
# . Divisibility check: Input a number and check if it is divisible by both 3 and 5.

def myDivisor (x):
  if x % 3 == 0 and x % 5 == 0:
   print("divisible")
  else:
   print ("not divisible")
myDivisor(99)
myDivisor(33)
myDivisor(14)
myDivisor(30)