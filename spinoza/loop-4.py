# Write a function, count_odds(vals), which returns the number of values v in vals which are odd

# count_odds([1,2,3,4,5]) --> 3
# count_odds([2,4,6,8]) --> 0
# count_odds([1,3,5,2,4,6,7]) --> 4

def count_odds(list):
    '''returns the number of values v in vals which are odd'''
    odd_number_list=[]
    for number in list:
        if number % 2 > 0:
            odd_number_list.append(number)
    return len(odd_number_list)


print(count_odds([1,3,5,2,4,6,7]))