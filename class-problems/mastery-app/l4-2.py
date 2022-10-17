# Complete this program

# '''
# score2grade
# returns your letter grade
# based on your numeric score from 0 to 100
# '''

# score = int(input("what is your score (out of 100)? "))

# if (score==100):
#     print("A+")
# elif (score >=93):
#     print('A')
# elif (score>=90):
#     print('A-')
# else:
#     print("Fail")
gradeScore = int(input("what is your score (out of 100)?"))

if(gradeScore==100):
    print("A+")
elif(gradeScore<=93 and gradeScore>=90):
    print("A")
elif(gradeScore<=90 and gradeScore>=89):
    print("A-")
elif(gradeScore<=89 and gradeScore>=83):
    print("B+")
elif(gradeScore <=83 and gradeScore>=80):
    print("B")
elif(gradeScore<=90 and gradeScore>=79):
    print("B-")
elif(gradeScore<=79 and gradeScore>=73):
    print("C+")
elif(gradeScore <=73 and gradeScore>=70):
    print("C")
elif(gradeScore<=70 and gradeScore>=69):
    print("C-")
elif(gradeScore<=69 and gradeScore>=63):
    print("D+")
elif(gradeScore <=63 and gradeScore>=60):
    print("D")
elif(gradeScore==60):
    print("D-")
else:
    print("Fail")

