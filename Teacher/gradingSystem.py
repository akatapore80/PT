# 1. Grading System with Multiple Ranges
# Write a program that takes a student’s score (0–100) and prints their grade and remark by concatenating the grade and remark:

# A if score ≥ 90
#  print("excellent")
# B if score ≥ 75 and < 90
# ("very good")
# C if score ≥ 60 and < 75
# print("good")
# D if score ≥ 50 and < 60
# print("average")
# F if score < 50
# print("failed")


student1 = 90
student2 = 65
student3 = 61
student4 = 42
student5 = 5
student6 = 0


def gradingSystem (studentGrade) : 

    if studentGrade >= 90 : 
      print(studentGrade, "excellent")
    elif studentGrade >= 75 and studentGrade < 90 : 
       print(studentGrade, "very good")
    elif studentGrade >= 60  and studentGrade < 75 : 
      print(studentGrade, "good")
    elif studentGrade >= 50 and studentGrade < 60 : 
      print(studentGrade, "average")
    else :
       print(studentGrade, "failed")


gradingSystem(student1)
gradingSystem(student2)
gradingSystem(student3)
gradingSystem(student4)
gradingSystem(student5)
gradingSystem(student6)

