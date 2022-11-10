# You are to write a program that quizzes students on a kind of algebra problem:
#     multiplication of binomials  (ax+b)*(cx+d)
# It should continue to do so until they want to stop and it should keep track of how many they ask and how many they get right.
# Also, the problems should be randomly generated with a,b,c,d in the range [-10,10] and you can construct the answer
#   u*x^2 + v*x +w
# where u = ac  v=ad+bc and w = bd


###TO DO###
# Create binomial_problem_maker that returns a randomly generated problem

def binomial_practice():
    '''Program to quiz students on binomial multiplication.'''
    program_state = True
    while (program_state == True):
        print("Hello")
        user_prompt_exit_game = input('Continue practicing?')
        if(user_prompt_exit_game=='Y'):
            continue
        elif(user_prompt_exit_game=='N'):
            program_state = False
    print("Goodbye")
    exit()

binomial_practice()