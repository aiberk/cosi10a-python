# Modify the code below to partly complete the function.
# In the case of a roll not equal to 2,3,7,11,12, don't continue rolling ... just print the message ..
import random   

def roll2dice():
    ''' simulates rolling 2 dice and returns the sum of the dice ... '''
    die1=random.randint(1, 6)
    die2=random.randint(1, 6)
    print("You rolled",die1,"and",die2,"total of",die1+die2)
    return die1+die2

def play1game():
    ''' simulates one game of craps and returns True if user wins, false if they lose
        and it prints out all of the rolls of the dice.
        
    '''
    roll1 = roll2dice()
    if(roll1==2 or roll1==3 or roll1==11 or roll1==12):
        print("Roll again...")
        play1game()
    elif(roll1==7):
        print("You Win")
    else:
        print("You Loose")
 
play1game()

