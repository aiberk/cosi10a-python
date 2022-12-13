# Write a function count_As(scores) which returns the number of A's in a list of test scores.

# So,  count_As([90,85,95,100,75,91])  returns 4
# and count_As([89,88,65,84]) returns 0

def count_As(scores):
    '''Returns the number of A's in a list ot test scores'''
    a_list = []
    for score in scores:
        if score >= 90:
            a_list.append(score)
    return len(a_list)

print(count_As([89,88,65,84]))
