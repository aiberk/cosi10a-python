# Write code to make this figure

# enter n: 4
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# enter n:3
# 1 1 1
# 2 2 2
# 3 3 3



def print_num():
    num = int(input("enter n: "))
    for x in range(1,num+1):
        for j in range(1,num+1):
            print(x,end=" ")
        print()

print_num()




