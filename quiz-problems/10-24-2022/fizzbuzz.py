# Write the fizzbuzz(n) function which returns
# 'fizzbuzz' if n is divisible by 15
# 'fizz' if n is divisible by 3 but not 5
# 'buzz' if n is divisible by 5 but not 3
# the number n, if n is not divisible by 3 or 5

# Don't forget the docstring!

def fizzbuzz(n):
    '''Returns combinations of 'fizz' and 'buzz' depending on n's divisibility '''
    if (n%15==0):
        return 'fizzbuzz'
    elif(n%5==0):
        return 'fizz'
    elif(n%3==0):
        return 'buzz'
    elif(n%3>0 or n%5>0):
        return n
print(fizzbuzz(15))
print(fizzbuzz(5))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(7))