# What is the sum of the numbers from 1 to 1 million?
# Write the python code to calculate it?

def sumUpto(number):
    i=0
    total=0
    while(i<=number):
        total=total+i
        i+=1
    print(total)

sumUpto(1000000)

# Answer 500000500000

# sum = 0
# for x in range(1, 1000001):
#     sum+=x
# print(sum)