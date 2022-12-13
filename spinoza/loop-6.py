# Write a function, sum_squares(vals), which returns the sum of the squares of all the numbers in the list vals.

# sum_squares([1,2,3]) --> 14
# sum_squares([-1,0,1]) --> 2
# sum_squares([1,3,5,7]) -->84

def sum_squares(list):
    '''returns the sum of the squares of all the numbers in the list vals'''
    square_sum=0
    for number in list:
        square_sum = square_sum + number**2
    return square_sum

print(sum_squares([1,2,3]))