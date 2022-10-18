# modify the roll2dice program so it also prints out the die values ... e.g.
import random   

def roll2dice():
    ''' simulates rolling 2 dice and returns the sum of the dice ... '''
    die1=random.randint(1, 6)
    die2=random.randint(1, 6)
    print("You rolled",die1,"and",die2,"total of",die1+die2)
    return die1+die2
    

roll2dice()
# > roll2dice()
# you rolled 3 and 5
# 8
# > roll2dice()
# you rolled 4 and 1
# 5