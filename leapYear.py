
year1 = 2025
year2 = 2400
year3 = 1966

def leapYear (year):
  if (year % 400 == 0 ):
    print("Leap year")
  elif (year % 4 ==0 and year % 100 != 0):
    print("Leap year")
  else :
    print("not leap year")
leapYear(year1)
leapYear(year2)
leapYear(year3)