# You are to write a program to play the game NIM against a user, as described below.

# You should solve this problem by writing a sequence of programs nim0.py, nim1.py, nim2.py, nim3.py, etc.
# following a top-down development style as shown in class, where each one is an extension of the previous one 
# that gets closer to the final product by defining and using new functions.

# What to submit:
# Submit all of the versions below, separated by lines of dashes '--------------------------------------------------'
# Also include a sample of game play for your final version.

# NIM is a game that starts with three positive numbers: a, b, and c
# Let's represent it by a dictionary nim_state={a:10, b:10, c:10}
# At each step a play picks a number (a, b, or c) and removes 1 or more from that number, possibly all.
# The loser is the person who takes the last number from the last peg.
# Your computer player can just randomly pick a number (a,b,c) which is not zero
# and then randomly pick some value to subtract from it (at least 1).

# Here is a link to a wikipedia article about NIM which also describes a winning strategy
# https://en.wikipedia.org/wiki/Nim
# If you want to implement the winning strategy you may, but you only need to implement
# the random strategy as described above for this assignment.

## nim-5.py
## Aby Iberkleid

## This is the sixth version of the NIM game program. 
# This version has the following improvements:
#   - The program's Computer has a moderate difficulty strategy: always play the peg with largest amount of rings
#   - and never leaves the the peg empty
#   - This program also catches bad user input with input_cleaner() to prevent unintentional programming halting 


import re

'''
NIM Game
'''

def play_nim():
    '''Game of nim'''
    nim_state={'a':10, 'b':10, 'c':10}
    turn_number_array = []
    nim_zero_array=[]
    line_separator='--------------------------------------------'

    def populate_nim_zero_array():
        '''Creates an array of precomputed nim sums that are equal to zero. For the computer's use in the game'''
        for x in range(11):
            for y in range(11):
                for z in range(11):
                    if(x^y^z==0):
                        nim_zero_array.append([x,y,z])
    
    def print_current_score():
        '''Prints current score'''
        print(f'NIM State: {nim_state}\n')

    def find_strategy(x,y,z):
        '''Goes through array of precomputed nim_zero computations to find next moves'''
        for item in nim_zero_array:
            if((item[0]==x and item[1]==y and item[2]<=z)):
                difference = z - item[2]
                return ['c',difference]
            elif((item[0]==x and item[2]==z and item[1]<=y)):
                difference = y - item[1]
                return ['b',difference]
            elif((item[1]==y and item[2]==z and item[0]<=x)):
                difference = x - item[0]
                return ['a',difference]

    def update_board(peg,number_to_remove):
        '''receives a peg and number_to_remove'''
        current = nim_state[peg]
        temp_amount = current-number_to_remove
        if(temp_amount<=0):
            final_amount = 0
        else:
            final_amount=temp_amount

        nim_state.update({peg:final_amount})
        return nim_state
    
    def declare_winner():
        '''Declares winner. The method used is by tracking all moves and then counting them.
        If there was an odd number of plays the second player loses and even for first player'''
        if(len(turn_number_array)%2==0):
            print('You win! Computer loses')
        elif(len(turn_number_array)%2==1):
            print('Computer wins! Player loses')
        print(line_separator)

    def player_move():
        '''Asks user to pick a move. The function corrects for any extra spaces and returns a tuple
        made out of a string and integer'''
        regex ='[abc]'
        regex2 = '[0-9]'
        user_input = input('your move: ')
        temp_variable = user_input.replace(" ", "")
        peg = re.findall(regex,temp_variable)
        temp_number_array = re.findall(regex2,temp_variable)
        if(len(peg)==0 or len(temp_number_array)==0):
            input_cleaner(user_input)
        amount_to_remove = int("".join(temp_number_array))
        print(f'removing {peg[0]} from {amount_to_remove} gives')
        return peg[0], amount_to_remove
    
    def input_cleaner(user_input):
        '''Warns a user the input is incorrect, and calls player_move() again for next attempt'''
        print(f'{user_input} is not an acceptable input please use \'a\', \'b\', or \'c\' + a number.')
        print("Example: a 12 or a12\n")
        player_move()
    

    populate_nim_zero_array()
    print(line_separator)
    print('Let\'s play NIM!')
    while(nim_state['a'] + nim_state['b'] + nim_state['c'] > 0):
        print_current_score()
        if(len(turn_number_array)%2==0):
            #USER TURN
            player_moves = player_move()
            peg = player_moves[0]
            amount_to_remove = player_moves[1]
            update_board(peg,amount_to_remove)
            turn_number_array.append([peg,amount_to_remove])
            print_current_score()
        elif(len(turn_number_array)%2 > 0):
             #COMPUTER TURN
            computer_moves = find_strategy(nim_state['a'],nim_state['b'],nim_state['c'])
            # print(computer_moves)
            peg = computer_moves[0]
            amount_to_remove = computer_moves[1]
            update_board(peg,amount_to_remove)
            turn_number_array.append([peg,amount_to_remove])
            print_current_score()
            

    declare_winner()
   
play_nim()

