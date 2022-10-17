# Write a program to print a table of the squares of the first 101 numbers, starting at 0 ending at 100
# 0 0
# 1 1
# 2 4
# 3 9
# ....
# 100 10000

def squaresUpto(number):
    i=0
    while(i<=number):
        print(i,i**2)
        i+=1
squaresUpto(101)

# for i in 100:
# print(i," ",i**2)