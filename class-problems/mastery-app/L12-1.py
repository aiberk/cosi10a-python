# Modify the code below so that it only prints words of length at least 4
# by adding an if statement and testing the length of words[index] with len(words[index])

def print_long_words(values):
    ''' prints the long words in a list, values, one per line with its index '''

    index = 0
    while index<len(values):
        if(len(values[index])>=4):
            print(index, values[index])
        index = index + 1
        

words = "this is a short sentence".split()

print_long_words(words)

# This should print the following
# 0 this
# 3 short
# 4 sentence