# You are to write a program that quizzes students on a kind of algebra problem:
#     multiplication of binomials  (ax+b)*(cx+d)
# It should continue to do so until they want to stop and it should keep track of how many they ask and how many they get right.
# Also, the problems should be randomly generated with a,b,c,d in the range [-10,10] and you can construct the answer
#   u*x^2 + v*x +w
# where u = ac  v=ad+bc and w = bd

###Final things todo - make 'loop' . in finalscore() to keep final score print funcitoning correctly
#### Add better LUI for users (Input Options)

import random


'''
Binomial Multiplication Practice
'''

def binomial_practice_program():
    '''Program to quiz students on binomial multiplication.'''
    #Global state variables, constants, and UI strings
    program_state = True
    user_answer =''
    correct_array = []
    wrong_array = []
    wrong_answers_array = []
    correct_answers_for_wrong =[]
    separator_lines = '------\n'
    input_warning_string = '(Please enter \'Y\' or \'y\' for YES, & \'N\' or \'n\' for NO)' 
    input_sample_string = '(example: x^2+x+1)' 

    def binomial_problem_factory():
        '''Function that creates a binomial problem and returns the problem and its answer'''
        #Assign random values to each variable in the equation
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)

        #Create variables to compute answer
        u = a*c 
        v = a*d+b*c
        w = b*d
        
        #Correct operators for negative values in string
        b_operator='+'
        d_operator='+'
        v_operator='+'
        w_operator='+'

        if(d<0):
            d_operator=''
        
        if(b<0):
            b_operator=''

        if(v<0):
            v_operator=''

        if(w<0):
            w_operator=''

        #create problem and answer strings for display and comparison
        #update global variables to share with other functions

        global answer_string
        answer_string = str(u) + 'x^2'+str(v_operator)+str(v)+'x'+str(w_operator)+str(w)

        global equation_string
        equation_string = '('+str(a)+'x'+str(b_operator)+str(b)+')'+'*'+'('+str(c)+'x'+str(d_operator)+str(d)+')'
        return answer_string, equation_string
    
    def answer_Tracker(user,answer,equation):
        '''Function compare the user's answer string against the correct answer string. Finally it adds the problem to a correct or incorrect array'''
        if(user==answer):
            correct_array.append(equation)
            print('That is correct!')
        else:
            wrong_array.append(equation)
            wrong_answers_array.append(user)
            correct_answers_for_wrong.append(answer)
            print('I am sorry, but',user,'is incorrect. The answer is:',answer,'\n')

    def final_score():
        '''Function that prints the final score and the specific problems the users correct and incorrect problems'''
        total_problems= len(correct_array) + len(wrong_array)
        print('')
        print('You answered',total_problems)
        print('Correct:',len(correct_array))
        print('Wrong:',len(wrong_array))
        print('')
        view_problems =input(f'Before you leave, would you like to print the problems you got wrong? {input_warning_string}\n')
        
        if(view_problems=='Y' or view_problems == 'y'):
            print('')
            print('You got these problems incorrect:')
            for x ,y, z in zip(wrong_array,wrong_answers_array,correct_answers_for_wrong):
                print('Problem:',x)
                print('Your Answer:',y)
                print('Correct Answer:',z)
                print('')
        elif(view_problems=='N'or view_problems=='n'):
            exit()
            
        
        
    # While loop that keeps track of state if the User wants to continue playing    
    while (program_state):
        print(separator_lines)
       
        user_prompt_exit_game = input(f'Want to practice binomial multiplication? {input_warning_string}\n')
        print('Total Problems:',len(correct_array)+len(wrong_array),'Correct:',len(correct_array),'Wrong:',len(wrong_array),'\n')
        
        if(user_prompt_exit_game=='Y' or user_prompt_exit_game=='y'):
            binomial_problem_factory()
            user_answer=input(f'What is the answer to:{str(equation_string)} {input_sample_string}\n')
            print(input_sample_string)
            answer_Tracker(user_answer,answer_string,equation_string)
            
        elif(user_prompt_exit_game=='N' or user_prompt_exit_game=='n'):
            program_state = False
        else:
            print(input_warning_string)
            user_prompt_exit_game = input(f'Want to practice binomial multiplication? {input_warning_string}\n')
    final_score()
    print('Goodbye!')
    exit()

binomial_practice_program()