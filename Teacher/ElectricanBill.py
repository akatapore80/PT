# 5. Electricity Bill Calculator

# Write a program that calculates electricity bill based on units consumed:

# First 100 units → ₦5 per unit

# Next 100 units → ₦7 per unit

# Beyond 200 units → ₦10 per unit

# Print the total bill.
   

#==== first solution 

def bill(first, next, beyond) : 
    totalBill = 0
    if first <= 100 :
       totalBill += (first * 5)
    if next > 100 and next <= 200 :
        totalBill += (next * 7)
    if beyond > 200 : 
        totalBill += (beyond * 10)
    print("Total is : ", totalBill)

bill(200, 105, 220)


# ===== second solution
# int total = 5;

# int total = 6


# total = 5
# total = 6

totalBill = 0

def myBilling(bill) : 
  global totalBill
  if bill <= 100 : 
    totalBill +=(bill * 5)
  elif bill > 100 and bill <= 200 :
    totalBill += (bill * 7)
  else :
    totalBill += (bill * 10)


myBilling(100)
myBilling(100)
myBilling(201)
print("my billing", totalBill)

# ================= advance method and scalable method

advanceTotal = 0
def myAdvanceBilling(bill)  : 
  if bill <= 100 : 
    return bill * 5
  elif bill > 100 and bill <= 200 :
   return bill * 7
  else :
    return bill * 10

advanceTotal += myAdvanceBilling(100)
advanceTotal +=  myAdvanceBilling(100)
advanceTotal +=  myAdvanceBilling(201)
advanceTotal += myAdvanceBilling(201)
print("my advance billing", advanceTotal)