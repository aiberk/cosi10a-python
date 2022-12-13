# Write a function sum_pos(vals) which returns the sum of all the positive values in vals.

# So, 
# sum_pos([5,-2,3,-4]) will return 8
# sum_pos([-1,-2,-3]) will return 0

def sum_pos(vals):
    '''Sums all positive values in a sequence/list'''
    sum = 0
    for element in vals:
        if element >=0:
            sum = sum + element
    return sum


