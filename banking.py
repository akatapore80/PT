
balance = 2500 
withdrawal = 2000
def banking(balance, withdrawal):
    
    if withdrawal  > balance:
        print("Insufficient fund")
    elif withdrawal % 100 != 0:
     print("Amount must be in multiples of 100")
    else:
     balance  -= withdrawal 
     print("Transactions successful")
     print("New balance:", balance )
     
banking(3000, 2850)