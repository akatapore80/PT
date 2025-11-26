

# 3. Grade Pass or Fail

# Ask the user to input their exam score.

# If the score is greater than or equal to 50, print "Pass". Otherwise, print "Fail"
score = input("Enter score")
score = int(input("Enter score"))
def grade(score):
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
grade(score)
