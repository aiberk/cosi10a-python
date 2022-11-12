# unscrambles

# Write a program which picks a random word from a list of words,
# then scrambles the letters
# and repeatedly asks the user to guess the word and
# checks to see if they got the right word.  There may be multiple ways
# to unscramble a sequence of letters to form a word in the list, but
# the user has to find the one the computer generates, e.g.
# 'aet'  could be 'eat' or 'tea' or 'eta'
# The user can first specify how many letters the words should have
# The user can also give up if they want

# The program should let the user continue until they want to quit and then tell them
# how many words they unscrambled of each length and how many they gave up on.




'''
Unscramble Game
'''
import random


def playScramble():
    '''Game that randmoly picks a word from a list of 100000 and then scambles it, finally it asks a user to guess the original word. '''
    wordfile = open('wordlist.txt','r')
    wordstring = wordfile.read()
    words = wordstring.split()

    def prompt_generator():
        '''Chooses a word arbritrarly, with a length chosen by the user, then scrambles it'''
        randomized_index = random.randint(0, len(words))
        chosen_word= words[randomized_index]
        scrambled_word = [*chosen_word]
        shuffled = random.sample(scrambled_word, len(scrambled_word))
        final_string = ''
        for x in shuffled:
            final_string = final_string + x
        print('Shuffled',final_string)
        print('Answer',chosen_word)

        # scrambled_word = random.shuffle(chosen_word_array)
        return final_string,chosen_word

    print(prompt_generator())


playScramble()