# Login system: Simulate a simple login by checking if username and password match predefined values.

defUserName = "dav"
defPassword = "1234"

def  loginFunction (userName, password) :
   if userName == defUserName and password == defPassword :
      print("Log in Successful")
   else : 
     print("incorrect password or username")


loginFunction("dav", "1234")
loginFunction("alhasan", "12r26")