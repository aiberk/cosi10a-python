# Your goal is to write the hangman game so that the game play is as shown below.
# Your program should first read in the leeds.txt word list available at this URL:
#     https://www.cs.brandeis.edu/~tim/cs10afall22/
# It should then play a round of hangman and repeatedly ask the user if they want to continue, until they say no.
# For each round of the game, it should pick a word from leeds.txt which has at least 5 letters and contains only lowercase letters.
# If they guess a letter they have already guessed, it should repeatedly prompt them to guess another letter.
# They have to guess the word and they can only make 7 incorrect guesses (i.e. letters that don't appear in the word.)
# Your output should be exactly as shown below (though with different words of course).

'''
Python Hangman Game
'''
import random
import re

wordfile = open('leeds.txt','r')
wordstring = wordfile.read()
words = wordstring.split()
game_words_array = []
# Create array with approved words
for word in words:
    if (len(word)>=5 and word.islower):
        game_words_array.append(word)

def pickword(list_of_words):
    '''Randomly picks word from list of words'''
    return random.choice(list_of_words)

def make_board(chosen_word):
    '''Creates prints game board'''
    for letters in chosen_word:
        hidden_answer = hidden_answer + "_"
    return (chosen_word,hidden_answer)

def update_board(answer,current_display,user_guess):
    current_display_array = list(current_display)
    for letter in answer:
        if letter == user_guess:
            index = answer.index(letter)
            current_display_array[index] = letter
    return "".join(current_display_array)
       
def playgame(board):
    answer = board[0]
    current_display = board[1]
    player_attempts = 0
    while(player_attempts < 7):
        print(answer)
        print(current_display,'\n')
        user_guess=input('Guess a letter')
        player_attempts = player_attempts + 1
        new_display = update_board(answer, current_display, user_guess)
        current_display = new_display
    

playgame(make_board(pickword(game_words_array)))
























# If you want you
# ----------------------------------------
# Hangman!
# guess the word one letter at a time
# ----------------------------------------
# _______
# 7 guesses left: 
# next guess: e
# yes! e appears 1 times

# ____e__
# 7 guesses left: e
# next guess: t
# sorry t is not in the word

# ____e__
# 6 guesses left: et
# next guess: a
# yes! a appears 1 times

# _a__e__
# 6 guesses left: aet
# next guess: o
# sorry o is not in the word

# _a__e__
# 5 guesses left: aeot
# next guess: i
# sorry i is not in the word

# _a__e__
# 4 guesses left: aeiot
# next guess: n
# yes! n appears 1 times

# _a__en_
# 4 guesses left: aeinot
# next guess: s
# yes! s appears 1 times

# _a__ens
# 4 guesses left: aeinost
# next guess: h
# sorry h is not in the word

# _a__ens
# 3 guesses left: aehinost
# next guess: r
# yes! r appears 1 times

# _ar_ens
# 3 guesses left: aehinorst
# next guess: d
# yes! d appears 1 times

# _ardens
# 3 guesses left: adehinorst
# next guess: l
# sorry l is not in the word

# _ardens
# 2 guesses left: adehilnorst
# next guess: w
# sorry w is not in the word

# _ardens
# 1 guesses left: adehilnorstw
# next guess: g
# yes! g appears 1 times

# !!!!!!!!!! You won! !!!!!!!!!!

# more? (y or n) y
# ______
# 7 guesses left: 
# next guess: e
# sorry e is not in the word

# ______
# 6 guesses left: e
# next guess: t
# yes! t appears 1 times

# ___t__
# 6 guesses left: et
# next guess: a
# sorry a is not in the word

# ___t__
# 5 guesses left: aet
# next guess: o
# sorry o is not in the word

# ___t__
# 4 guesses left: aeot
# next guess: i
# yes! i appears 1 times

# __it__
# 4 guesses left: aeiot
# next guess: n
# sorry n is not in the word

# __it__
# 3 guesses left: aeinot
# next guess: s
# yes! s appears 1 times

# s_it__
# 3 guesses left: aeinost
# next guess: h
# yes! h appears 1 times

# s_it_h
# 3 guesses left: aehinost
# next guess: r
# sorry r is not in the word

# s_it_h
# 2 guesses left: aehinorst
# next guess: d
# sorry d is not in the word

# s_it_h
# 1 guesses left: adehinorst
# next guess: l
# sorry l is not in the word

# !!!!!!!!!! You lost. !!!!!!!!!!
# The word was switch

# more? (y or n) y
# _____
# 7 guesses left: 
# next guess: e
# sorry e is not in the word

# _____
# 6 guesses left: e
# next guess: e
# you've already guessed e
# pick a letter not in e
# try again: t
# sorry t is not in the word

# _____
# 5 guesses left: et
# next guess: a
# sorry a is not in the word

# _____
# 4 guesses left: aet
# next guess: o
# yes! o appears 1 times

# __o__
# 4 guesses left: aeot
# next guess: i
# sorry i is not in the word

# __o__
# 3 guesses left: aeiot
# next guess: n
# sorry n is not in the word

# __o__
# 2 guesses left: aeinot
# next guess: s
# sorry s is not in the word

# __o__
# 1 guesses left: aeinost
# next guess: h
# sorry h is not in the word

# !!!!!!!!!! You lost. !!!!!!!!!!
# The word was proxy

# more? (y or n) n
# bye