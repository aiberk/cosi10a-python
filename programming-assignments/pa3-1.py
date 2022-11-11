# You are to write a program that quizzes students on a kind of algebra problem:
#     multiplication of binomials  (ax+b)*(cx+d)
# It should continue to do so until they want to stop and it should keep track of how many they ask and how many they get right.
# Also, the problems should be randomly generated with a,b,c,d in the range [-10,10] and you can construct the answer
#   u*x^2 + v*x +w
# where u = ac  v=ad+bc and w = bd


###TO DO###
# Create binomial_problem_maker that returns a randomly generated problem
# Get global variables to update
# add logic for operators in bpf func - Done

import random

def binomial_practice():
    '''Program to quiz students on binomial multiplication.'''
    #Global state variables
    program_state = True
    user_answer =''
    correct_array = []
    wrong_array = []
    total_problems = 0
    separator_lines = '<-------------------------------->\n'

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
        
        #Correct operators in string
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
        '''Function checks if the user got the answer right and adds it to a correct or wrong array'''
        if(user==answer):
            correct_array.append(equation)
            print('That is correct!')
        else:
            wrong_array.append(equation)
            print('I am sorry, but that is incorrect. The answer is:',answer,'\n')

    def final_score():
        global total_problems
        total_problems= len(correct_array) + len(wrong_array)
        print('You answered',total_problems)
        print('Correct:',len(correct_array))
        print('Wrong:',len(wrong_array))

        
        
    # While loop that keeps track of state if the User wants to continue playing    
    while (program_state == True):
        print('Total Problems:',len(correct_array)+len(wrong_array),'Correct:',len(correct_array),'Wrong:',len(wrong_array))
        user_prompt_exit_game = input('Continue practicing?\n')
        
        if(user_prompt_exit_game=='Y' or user_prompt_exit_game=='y'):
            binomial_problem_factory()
            print(separator_lines)
            #for testing get rid
            print("For testing",answer_string)
            user_answer=input('What is the answer to:'+ str(equation_string)+"\n")
            answer_Tracker(user_answer,answer_string,equation_string)
            #continue
        elif(user_prompt_exit_game=='N' or user_prompt_exit_game=='n'):
            program_state = False
    final_score()
    exit()

binomial_practice()