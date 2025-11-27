num1 = input("Enter any number either poositive or negative")
convertNum1 = int(num1)
def greaterThan(m):
  if m > 0:
   print("Positive number")
   if m > 100:
    print("Positive number and greater than 100")
   else:
    print("Posive but not greater than 100")
  else:
   print("Not positive number")

greaterThan(convertNum1)