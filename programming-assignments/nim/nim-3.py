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

## nim-3.py
## Aby Iberkleid


## This is the third version of the NIM game program. 
# This version has the following improvements:
#   - The program accepts any combination of inputs from user. example: ('a10','a 10','10a','10 a')

# TODO
# improve computer strategy in new function called strategic_computer_play()
# always take from biggest of three pegs. 

import random
import re

def play_nim():
    '''Game of nim'''
    nim_state={'a':10, 'b':10, 'c':10}
    turn_number_array = []
    regex ='[abc]'
    regex2 = '[0-9]'
    line_separator='--------------------------------------------'

    def print_current_score():
        '''Prints current score'''
        print(f'NIM State: {nim_state}\n')

    def computer_play():
        '''Simple AI to play nim. Arbitrarily picks a peg, checks how many left on the peg, again arbitrarily  
        picks an amount to remove. Finally returns the peg and number to remove from the peg'''
        randomized_index = random.randint(0, 2)
        peg = ''
        if(randomized_index == 0):
            peg = 'a'
        elif(randomized_index == 1):
            peg='b'
        elif(randomized_index == 2):
            peg='c'
        number_to_remove = random.randint(1, 10)
        print(f'Computer move: {peg} {number_to_remove}')
        print(f'removing {number_to_remove} from {peg} gives')
        return [peg, number_to_remove]

    def strategic_computer_play():
        '''Simple but logical AI to play nim. Picks peg with most rings, then arbitrarily picks an amount to remove. 
        Finally returns the peg and number to remove from the peg'''
        peg = ''
        if(nim_state['a'] >= nim_state['b'] and nim_state['a'] >= nim_state['c']):
            peg = 'a'
        elif(nim_state['b'] >= nim_state['a'] and nim_state['b'] >= nim_state['c']):
            peg='b'
        elif(nim_state['c'] >= nim_state['a'] and nim_state['c'] >= nim_state['b']):
            peg='c'
        number_to_remove = random.randint(1, 10)
        print(f'Computer move: {peg} {number_to_remove}')
        print(f'removing {number_to_remove} from {peg} gives')
        return [peg, number_to_remove]
    
    def update_board(peg,number_to_remove):
        '''receives a peg and number_to_remove'''
        current = nim_state[peg]
        nim_state.update({peg:current-number_to_remove})
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
        temp_variable = input('your move: ').replace(" ", "")
        peg = re.findall(regex,temp_variable)
        amount_to_remove = int("".join(re.findall(regex2,temp_variable)))
        print(f'removing {peg[0]} from {amount_to_remove} gives')
        return peg[0], amount_to_remove
        
    
    print(line_separator)
    print('Let\'s play NIM!')
    while(nim_state['a'] > 0 and nim_state['b'] > 0 and nim_state['c'] > 0):
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
            computer_moves = strategic_computer_play()
            peg = computer_moves[0]
            amount_to_remove = computer_moves[1]
            update_board(peg,amount_to_remove)
            turn_number_array.append([peg,amount_to_remove])
            print_current_score()

    declare_winner()
   
play_nim()

