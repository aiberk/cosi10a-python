# write a function clamp(x) which return 0 if x is negative and returns 100 if x is bigger than 100,
#  and returns x otherwise, i.e. it makes sure that its result is between 0 and 100 inclusive.

# For example,
# clamp(-5) --> 0
# clamp(0) --> 0
# clamp(99) --> 99
# clamp(1) --> 1
# clamp(100) --> 100
# clamp(1000) --> 100

def clamp(x):
    '''returns 0 if x is negative and returns 100 if x is bigger than 100,
and returns x otherwise'''
    if x<=0:
        return 0
    elif x>=100:
        return 100
    else:
        return x

print(clamp(900))
print(clamp(-900))
print(clamp(100))
print(clamp(0))
print(clamp(1))
print(clamp(99))

print(clamp(-5))