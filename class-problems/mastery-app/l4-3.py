# Write a script that asks their age:
# child < 12)
# adult
# senior>=65
# and then gives them the ticket price
# $5 kids
# $15 adults
# $10 seniors

# How old are you? 67
# Your ticket is $10
# ]

age = int(input("what is your age in year?"))

if (age <= 12):
    print("Kid ticket is $10")
elif(age >12 and age <65):
    print("Adult ticket is $15")
else:
    print("Senior ticket is $10")
