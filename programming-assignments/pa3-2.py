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

####TO DO######
###Add symbols to REGEX
###Fix total counter


'''
Unscramble Game
'''
import random
import re


def play_word_scramble():
    '''Game that randomly picks a word from a list and then scrambles it, finally it asks a user to guess the original word. '''

    #Global state variables, constants, and UI strings
    program_state =True
    correct_array = []
    wrong_array = []
    attempts_array = []
    regex = '^[a-zA-Z]*$'
    input_warning_string ='(Please enter \'Y\' or \'y\' for YES, & \'N\' or \'n\' for NO or type \'exit\' to quit)' 
    exit_string = '(type \'exit\' to quit game)'

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
        '''Filter method for filter() function. Gets array of words and returns a new array 
        containing words with the user defined length'''
        if(len(word)==int(user_word_length_choice)):
            return True
        else:
            return False

    def space():
        '''Function that prints extra spaces for LUI'''
        print('')
    
    def round_and_score_control(filtered_word_list):
        '''Receives a tuple from prompt_generator() containing a string and a shuffled version of that string's characters. 
        It then asks the user to guess the original string by printing out the shuffled version. 
        After getting input back from the user it checks if the user_guess and original string match. '''
        user_success=False
        prompt = filtered_word_list[0]
        answer = filtered_word_list[1]
        while(user_success==False):
            ##DEBUG PRINT##
            # print(prompt, answer)
            user_guess=input(f'What is the original sequence/word for {prompt}? {exit_string}\n')
            if(user_guess==answer):
                attempts_array.append(1)
                correct_array.append(answer)
                print('\nNice!',answer,'is correct!!')
                print_final_score(correct_array,wrong_array,attempts_array)
                user_success = True
            elif(user_guess =='exit'):
                exit()
            else:
                attempts_array.append(prompt)
                wrong_array.append([prompt,answer])
                user_success=try_again(answer,prompt,user_guess)
    
    def try_again(answer,prompt,user_guess):
        '''Handles trying a problem n times. Returns user_success==False to try again, 
        and user_success=True to stop.' '''
        block_complete = False
        print(f'{user_guess} is incorrect :(')
        while(block_complete == False):
            try_again = input(f'\nWant to try again? {exit_string}\n')
            if(try_again=='N' or try_again=='n'):
                wrong_array.append([prompt,answer])
                print('\nThe answer was:',answer)
                print_final_score(correct_array,wrong_array,attempts_array)
                return True
            elif(try_again=='Y' or try_again=='y'):
                return False
            elif(try_again =='exit'):
                exit()
            else:
                print(f'\n{input_warning_string}')
                continue
            
            

    def print_final_score(correct, wrong, attempts):
        '''Prints score between rounds and at end of the game. 
        Receives three arguments, the correct_answers array, wrong_answers array, and attempts_array'''
        total = len(correct) + len(wrong)
        print('\nYou played a total of:',total,'words')
        print('You got',len(correct),'correct, you got',len(wrong),'incorrect')
        print('and attempted a total of:',len(attempts),'times \n')
     
    
    
    def input_cleanser():
        '''(TLDR avoid Type errors) Gets input from user and makes sure it is the right type (), 
        if the input is NOT the right type it will prompt user again'''
        input_clean = False
        message = 'please add a number between 1-20'
        global user_word_length_choice
        while(input_clean==False):
            user_word_length_choice = input('What word length?(20 MAX)\n')
            input_checker = re.search(regex,user_word_length_choice)
            if(input_checker):
                print('\nLetters are not permitted,',message, '\n')
            elif(int(user_word_length_choice)>=20):
                print('\n20 is the maximum word length,',message,'\n')
            else:
                return user_word_length_choice
        
    while(program_state):
       
        if(len(attempts_array)==0):
            user_prompt_game_state = input(f'\nWant to play WORD-SCRAMBLE? {exit_string}\n')
        else:
            user_prompt_game_state = input(f'Want to play WORD-SCRAMBLE again? {exit_string} \n')
        space()
        if(user_prompt_game_state=='Y'or user_prompt_game_state=='y' or user_prompt_game_state=='YES' or user_prompt_game_state=='yes'):
            input_cleanser()
            space()
            round_and_score_control(prompt_generator())
        elif(user_prompt_game_state=='N' or user_prompt_game_state=='n' or user_prompt_game_state=='NO' or user_prompt_game_state=='no'):
            space()
            print(f'Thank you for playing WORD-SCRAMBLE!')
            print_final_score(correct_array,wrong_array,attempts_array)
            program_state = False
        elif(user_prompt_game_state =='exit'):
            exit()
        else:
            print(input_warning_string)
            program_state = True

    print('Goodbye!')
    exit()



    

play_word_scramble()