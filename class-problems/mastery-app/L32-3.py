# Write the code for this figure:

# enter n: 4
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16


# enter n: 3
#  1  2  3
#  4  5  6
#  7  8  9

def print_figure():
    num = int(input("enter n: "))
    for x in range(1,num+1):
        for j in range(1,num+1):
            print(x,end=" ")
        print()

print_figure()