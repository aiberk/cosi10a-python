# write a script which counts up from 1 to 100
# (don't write 100 print statements!)
# It should print
# hello 1
# hello 2
# ....
# hello 100
# goodbye


# Here is the code for counting down from 100:

# n=100
# while n>0:
#     print('hello',n)
#     n = n - 1
# print('goodbye')

def countUpTo(number):
    i =1
    while (i<=number):
        print('hello',i)
        i+=1
    print('goodbye')
countUpTo(10)