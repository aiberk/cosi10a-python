# Write a function, filter_long_words(words,n), which will return a list of all the words in the argument that are at least n characters long.

# For example, this code
# a1=['A','road','diverged','in','a','yellow','wood'];
# filter_long_words(a1,4) -->  ['road','diverged','yellow','wood'] 

a1=['A','road','diverged','in','a','yellow','wood']

def filter_long_words(words,n):
    '''Returns a list of all the words in the argument that are at least n characters long'''
    long_words_list =[]
    for word in words:
        if len(word)>=n:
            long_words_list.append(word)
    return long_words_list

print(filter_long_words(a1,5))
