# write a procedure fizzbuzz(N) which prints out the numbers from 1 to N, each on its own line,
#  but when N is a multiple of 3 it prints "fizz", when a multiple 5 it prints "buzz" and a multiple
#  of 15 it prints "fizzbuzz".

def fizzbuzz(n):
    '''prints out the numbers from 1 to N, each on its own line,
but when N is a multiple of 3 it prints "fizz", when a multiple 5 it prints "buzz" and a multiple
of 15 it prints "fizzbuzz"'''
    for number in range(n):
        if number == 0:
            continue
        elif(number>=15 and number%15==0):
            print("fizzbuzz")
        elif(number%5==0):
            print("buzz")
        elif(number%3==0):
            print("fizz")
        else:
            print(number)
fizzbuzz(100)

# print(10%5)
# print(10%3)
# print(5%15)
# print(36%15)