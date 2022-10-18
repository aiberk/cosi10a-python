# Complete the code below to write the function to simulate rolling 2 dice and returning the sum

# '''
# craps.py is an interactive program to play a simple version of the dice game craps

# '''
import random   # randint(a,b) returns random integer between a, b inclusive

def roll2dice():
    ''' simulates rolling 2 dice and returns the sum of the dice ... '''
    die1=random.randint(1, 6)
    die2=random.randint(1, 6)
    print(die1+die2)

roll2dice()

    