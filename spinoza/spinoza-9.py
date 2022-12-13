# Write a function oddeven(n) which returns the string 'odd' if n is an odd number and 'even' if it is an even number.

# For example,
# oddeven(4) --> 'even'
# oddeven(17) --> 'odd'
# oddeven(0) --> 'even'

# Remember that you can test if a number is even by seeing if the remainder of division by 2 is 
# zero and we use the percent sign to take remainders...
# 11%2 --> 1
# 13%10 --> 3

def oddeven(n):
    '''returns the string 'odd' if n is an odd number and 'even' if it is an even number'''
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'
print(oddeven(4)) 
print(oddeven(17)) 
print(oddeven(0))