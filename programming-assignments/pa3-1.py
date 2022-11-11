# You are to write a program that quizzes students on a kind of algebra problem:
#     multiplication of binomials  (ax+b)*(cx+d)
# It should continue to do so until they want to stop and it should keep track of how many they ask and how many they get right.
# Also, the problems should be randomly generated with a,b,c,d in the range [-10,10] and you can construct the answer
#   u*x^2 + v*x +w
# where u = ac  v=ad+bc and w = bd


###TO DO###
# Create binomial_problem_maker that returns a randomly generated problem

import random

def binomial_practice():
    '''Program to quiz students on binomial multiplication.'''
    program_state = True
    equation_string ='nothing'
    answer_string=''

    def binomial_problem_factory():
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        u = a*c 
        v = a*d+b*c
        w = b*d
        temp = str(u) + 'x^2'+str(v)+'x'+str(w)
        global equation_string
        equation_string = temp

        global answer_string
        answer_string = '('+str(a)+'x+'+str(b)+')'+'*'+'('+str(c)+'x+'+str(d)+')'
        print('')
        print('What is the solution to:')
        print(answer_string)
        print('')
        print(equation_string)
        
        
        
    while (program_state == True):
        user_prompt_exit_game = input('Continue practicing?')
        
        if(user_prompt_exit_game=='Y' or user_prompt_exit_game=='y'):
            print('Previous Equation',answer_string)
            binomial_problem_factory()
            continue
        elif(user_prompt_exit_game=='N' or user_prompt_exit_game=='n'):
            program_state = False
    print("Goodbye")
    exit()

binomial_practice()