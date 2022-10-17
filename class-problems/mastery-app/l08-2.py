# '''
# hailstone sequence ...
# ask for a positive integer n
# If it is even (ie. n%2==0) divide it by 2
# if it is odd, multiply by 3 and add 1
# e.g with n=5 we get
# 5 16 8 4 2 1 4 2 1 4 2 1 ....
# write the code to print the hailstone sequence
# use print(..., end=' ') to put the numbers all on one line
# Stop when  you reach n=1.
# '''

# n = input("enter n: ")

def hailstone():
     input_number = int(input("Enter a positive integer:"))
     print(input_number, end=' ')
     while (input_number>1):
        if(input_number%2==0):
            input_number=input_number/2
            print(input_number, end=' ')
        else:
            input_number=(input_number*3)+1
            print(input_number, end=' ')
hailstone()


