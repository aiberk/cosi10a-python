# Finish this code to play one round of RPS
# It should print

# I won
# You won
# or
# We tied

'''
Rock Paper Scissors game
'''
import random

print('Let\'s play Rock, Paper, Scissors')

choice = random.choice(['rock','paper','scissors'])
print(choice)
userchoice = input("Pick one?  (rock, paper, or scissors)")
score =''

if(choice == userchoice):
    score = 'We Tied'
elif(choice == 'rock' and userchoice =='scissors'):
    score = 'Computer Wins'
elif(choice == 'scissors' and userchoice =='rock'):
    score = 'User Wins'
elif(choice == 'rock' and userchoice =='paper'):
    score = 'User Wins'
elif(choice == 'paper' and userchoice =='rock'):
    score = 'Computer Wins'
elif(choice == 'scissors' and userchoice =='paper'):
    score = 'Computer Wins'
elif(choice == 'paper' and userchoice =='scissors'):
    score = 'User Wins'


print("User:",userchoice,"Computer:",choice,"Result:",score)