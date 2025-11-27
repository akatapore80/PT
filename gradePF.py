

# 3. Grade Pass or Fail

# Ask the user to input their exam score.

# If the sco is greater threan or equal to 50, print "Pass". Otherwise, print "Fail"
score = input("Enter score")
score = int(score)
def grade(score):
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
grade(score)
