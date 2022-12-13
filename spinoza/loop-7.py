# You're going to think like DNA! Let's start with the basic DNA replication. 
# First you need to check if you are looking at a DNA molecule. DNA is composed 
# only of A, T, C and G. Write a function, DNA_checker, that takes in a string of letters. 
# Return True if the string contains only A, T, C, and G, and False otherwise. Assume you are only passed in capital letters. 

# For example, DNA_checker("ACCCCG") will return True
# DNA_checker("AXFFG") will return False, since X and F are invalid characters.

import re

def DNA_checker(string):
    '''checks if you are looking at a DNA molecule by looking for exclusivley A,T,C, and G'''
    regex = re.findall("[BDEFHIJKLMNOPQRZUXWXYZ1234567890]", string)
    if len(regex)>0:
        return False
    else:
        return True

print(DNA_checker("ACCCCG"))
print(DNA_checker("AXFFG"))