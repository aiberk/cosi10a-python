# write a function can_vote(age) which returns true if a US citizen of the specified can vote. ie. 
# if they are at least 18 years old

# For example,
# can_vote(18) --> True
# can_vote(17) --> False
# can_vote(61) --> True
# can_vote(1) --> False

def can_vote(age):
    '''returns true if a US citizen of the specified can vote. ie. if they are at least 18 years old'''
    if(age>=18):
        return True
    else:
        return False
print(can_vote(18))
print(can_vote(17))
print(can_vote(81))