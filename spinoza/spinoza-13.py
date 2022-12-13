# Write a function continuous_interest(p,r,t) which calculates the balance in a bank account which 
# starts off with p dollars and then earns continuous interest at the annual rate of r percent for t years.  
# The formula is
#   p exp(rt)
# where exp is the exponential function (math.exp)
import math
def continuous_interest(p,r,t):
    '''which calculates the balance in a bank account which 
    starts off with p dollars and then earns continuous interest at the annual rate of r percent for t years.'''
    return p*math.exp(r*t)



