# Nested condition example: Input a number and check if it is positive; if positive, further check if it is greater than 100.

def greaterThan(m):
  if m > 0:
   print("Positive number")
   if m > 100:
    print("Positive number and greater than 100")
   else:
    print("Posive but not greater than 100")
  else:
   print("Not positive number")

greaterThan(120)
