# ''' complete this program
#     cut/paste in the play_craps function
#  '''

'''
craps.py is an interactive program to play a simple version of the dice game craps

'''
from random import randint   # randint(a,b) returns random integer between a, b inclusive
def roll2dice():
    "roll 2 dice and return the sum of it"
    first_dice=randint(1,6)
    second_dice=randint(1,6)
    sum=first_dice+second_dice
    print("you row a",first_dice,"and a", second_dice)
    return sum

def play1game():
    ''' simulates one game of craps and returns True if user wins, false if they lose
        and it prints out all of the rolls of the dice.
        
    '''
    roll1=roll2dice()
    if roll1== 2 or roll1==3 or roll1==12:
        print('you lose')
        return False
    elif roll1==7 or roll1==11:
        print('you win')
        return True
    else:
        print(f'you must roll a {roll1} before a 7')
        result = play_rest_game(roll1)
        return result

def play_rest_game(point):
    ''' returns True if they roll the point before a 7, False otherwise '''
    roll = roll2dice()
    while roll != point and roll!=7:
        roll=roll2dice()
    if roll==point:
        print('you win!')
        return True
    else:
        print("you lose")
        return False

def play_craps():
    ''' repeatedly asks the user if they want to play
        if so, it calls play1game()
        and continues until they don't want to play anymore
    '''

play1game()