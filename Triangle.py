
def Triangle (length1, length2, length3):
      if length1 == length2 == length3:
        print("Equilateral triangle")
      elif length1 == length2 or length1 ==length3 or length2 ==length3:
        print("Isosceles triangle")
      elif length1 != length2 != length3:
         print("Scalene triangle")
      else:
        print("Not a valid triangle")
Triangle(1,4,16)
Triangle(4,4,4)