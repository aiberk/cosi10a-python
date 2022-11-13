# unscrambles

# Write a program which picks a random word from a list of words,
# then scrambles the letters
# and repeatedly asks the user to guess the word and
# checks to see if they got the right word.
# 
#   There may be multiple ways
# to unscramble a sequence of letters to form a word in the list, but
# the user has to find the one the computer generates, e.g.
# 'aet'  could be 'eat' or 'tea' or 'eta'
# The user can first specify how many letters the words should have
# The user can also give up if they want

# The program should let the user continue until they want to quit and then tell them
# how many words they unscrambled of each length and how many they gave up on.

####TODO######
##add ability to choose length of new word, pass it to prompt_generator() as an argument. 
###Fix try again loop
###3INPUT cleansing for letter in lenght (use regex) and try again loop


'''
Unscramble Game
'''
import random


def play_word_scramble():
    '''Game that randomly picks a word from a list of 100000 and then scrambles it, finally it asks a user to guess the original word. '''

    #Global state variables, constants, and UI strings
    program_state =True
    correct_array = []
    wrong_array = []
    attempts_array = []
    wrong_answers_array = []
    correct_answers_for_wrong =[]
    input_warning_string = '(Please enter \'Y\' or \'y\' for YES, & \'N\' or \'n\' for NO)' 
    separator_lines = '------\n'

     #Load word dictionary ONE time when initialized to avoid reopening and closing
    wordfile = open('wordlist.txt','r')
    wordstring = wordfile.read()
    words = wordstring.split()

    def prompt_generator():
        '''Chooses a word arbritrarly, with a length chosen by the user, then scrambles it'''
        filtered_words = list(filter(filter_list, words))
        randomized_index = random.randint(0, len(filtered_words))
        chosen_word= filtered_words[randomized_index]
        scrambled_word = [*chosen_word]
        shuffled = random.sample(scrambled_word, len(scrambled_word))
        final_string = ''
        for x in shuffled:
            final_string = final_string + x
        return final_string,chosen_word
    
    
    def filter_list(word):
        '''Filter method for filter() function. Gets array of words and returns a new array containing words with the user defined length'''
        if(len(word)==user_word_length_choice):
            return True
        else:
            return False

    
    def round_and_score_control(filtered_word_list):
        '''Receives a tuple from prompt_generator() containing a string and a shuffled version of that string's characters. 
        It then asks the user to guess the original string by printing out the shuffled version
        as a hint. After getting input back from the user it checks if the user_guess and original string match, 
        if they don't the user is given as many chances as they like to guess. Once the guess is satisfactory 
        or the user chooses to give up, the function gives back control to the main while loop'''
        user_success=False
        prompt = filtered_word_list[0]
        answer = filtered_word_list[1]
        while(user_success==False):
            print(prompt, answer)
            user_guess=input(f'What is the original sequence for {prompt}?\n')
            if(user_guess==answer):
                attempts_array.append(1)
                correct_array.append(answer)
                print('')
                print('Nice!',answer,'is correct!!')
                user_success = True
            else:
                attempts_array.append(1)
                print('')
                try_again = input('Want to try again?\n')
                #@@add while loop here
                if(try_again=='N' or try_again=='n'):
                    wrong_array.append(1)
                    print('')
                    print('The answer was:',answer)
                    print_final_score(correct_array,wrong_array,attempts_array)
                    user_success =True
                elif(try_again=='Y' or try_again=='y'):
                    user_success==False
                else:
                    print(input_warning_string)
        

    def print_final_score(correct, wrong, attempts):
        '''Prints score between rounds and at end of the game. 
        Receives three arguments, the correct_answers array, wrong_answers array, and attempts_array'''
        total = len(correct) + len(wrong)
        print('')
        print('You played a total of:',total,'words')
        print('You got',len(correct),'correct, you got',len(wrong),'incorrect')
        print('and attempted a total of:',len(attempts),'times')
        print('')

        
    while(program_state):
        print('')
        if(len(attempts_array)==0):
            user_prompt_game_state = input('Want to play WORD-SCRAMBLE?\n')
        else:
            user_prompt_game_state = input('Want to play WORD-SCRAMBLE again?\n')
        print('')
        if(user_prompt_game_state=='Y'or user_prompt_game_state=='y'):
            global user_word_length_choice
            user_word_length_choice = int(input('Maximum word length?(25MAX)\n'))
            if(user_word_length_choice>25):
                print('')
                print('25 is the maximum word length')
                user_word_length_choice = int(input('What word length would you like to use?(25MAX)\n'))
            print('')
            round_and_score_control(prompt_generator())
        elif(user_prompt_game_state=='N' or user_prompt_game_state=='n'):
            print('')
            print(f'Thank you for playing WORD-SCRAMBLE!')
            print_final_score(correct_array,wrong_array,attempts_array)
            program_state = False
        else:
            print(input_warning_string)
            program_state = True

    print('Goodbye!')
    exit()



    

play_word_scramble()