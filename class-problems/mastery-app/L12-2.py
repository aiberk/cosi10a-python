# Rewrite print_long_words using a for loop

# def print_long_words(values):
#     '''prints the elements of a list, values one per line with its index'''
#     index = 0
#     while index < len(values):
#         if(len(words[index]) >= 4):
#             print(index, values[index])
#         index = index + 1
words = "this is a short sentence".split()
def print_long_words(values):
    '''prints the elements of a list, values one per line with its index'''
    index = 0
    for x in words:
        if(len(words[index]) >= 4):
            print(index, values[index])
        index = index + 1
        
print_long_words(words)