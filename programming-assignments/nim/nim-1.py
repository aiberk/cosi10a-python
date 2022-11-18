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

import random

def play_nim():
    '''Game of nim'''
    nim_state={'a':10, 'b':10, 'c':10}

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
        number_to_remove = random.randint(1, nim_state[peg])
        return [peg, number_to_remove]
    
    def update_board(peg,number_to_remove):
        '''receives a peg and number_to_remove'''
        ### subtract number to remove from original
        current = nim_state[peg]
        nim_state.update({peg:current-number_to_remove})
        return nim_state

    while(nim_state['a'] > 0 or nim_state['b'] > 0 or nim_state['c'] > 0):
        turn_number = 0
        if(turn_number%2==0):
            peg = input('Pick peg a, b, or c\n')
            amount_to_remove = int(input(f'How many rings to remove from peg {peg}?\n'))
            update_board(peg,amount_to_remove)
            print(f'Your move is {peg} {amount_to_remove}')
            print(nim_state)
            turn_number += 1
        elif(turn_number%2 > 0):
            computer_moves = computer_play()
            update_board(computer_moves[0],computer_moves[1])
            print(f'Computer move is {computer_moves[0]} {computer_moves[1]}')
            print(nim_state)
            turn_number += 1
   
    print(nim_state['a'],nim_state['b'],nim_state['c'])
    test = computer_play()
    print(update_board(test[0],test[1]))
    test2 = computer_play()
    print(update_board(test2[0],test2[1]))
  
    ### while a,b,c are >0
    ### player 1 pick peg
    ### player 1 remove peg
    ### check & update state
    ### computer check smallest peg
    ### computer remove random(1 to peg_rings) from peg
    ### check & update state

play_nim()

