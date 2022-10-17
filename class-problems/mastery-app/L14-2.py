# Modify the code below so that it creates two lists. 
# one of the even numbers and another of the odd numbers
# and prints them both out. You can test if a number n 
# is even using  n%2==0

# vals = []  # accumulator variable
# val = int(input("enter an integer: "))
# while val>0:
#     vals.append(val)
#     val = int(input("enter another integer, 0 to stop: "))
# vals.reverse()
# print(vals)

# Hint: have two accumulator variables
# even_vals=[]
# odd_vals=[]
# and append val to the appropriate one in the loop
import random
rgnList=[40, 68, 71, 91, 29, 37, 9, 37, 77, 53]
oddVals=[]
evenVals=[]
def seperateOddsAndEvens():
    '''Creates a random list of ten integers between 1-100 and separates them between odd and even'''
    list =[]
    i=0
    while(i<10):
        x=random.randint(0,100)
        list.append(x)
        i+=1

    for x in list:
        if(x%2==0):
            evenVals.append(x)
        else:
            oddVals.append(x)
    print("Original List:",list)
    print("Odd Values:",oddVals)
    print("Even Values:",evenVals)

# def randomNumberList():
#     '''creates a list of 10 random integers from 0-100'''
#     list =[]
#     i=0
#     while(i<10):
#         x=random.randint(0,100)
#         list.append(x)
#         i+=1
#     print(list)

# randomNumberList()
seperateOddsAndEvens()