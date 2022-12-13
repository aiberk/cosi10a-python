# Write a function, sum_odds(vals), which returns the sum of the odd numbers in vals

# sum_odds([1,2,3,4,5]) --> 9
# sum_odds([2,4,6,8]) --> 0
# sum_odds([1,3,5,2,4,6,7]) --> 16

def sum_odds(list):
    '''returns the sum of values v in vals which are odd'''
    odd_number_sum=0
    for number in list:
        if number % 2 > 0:
            odd_number_sum = odd_number_sum + number
    return odd_number_sum

print(sum_odds([1,2,3,4,5]))
print(sum_odds([2,4,6,8]))
print(sum_odds([1,3,5,2,4,6,7]))