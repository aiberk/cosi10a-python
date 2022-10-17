# Write the python code to split a string with words 
# separated by commas, into a list of words ...

# e.g. 
# x ="this, is, a, short, sentence'
# it will generate ['this', 'is','a', 'short','sentence']

# use split

sentence ="this, is, a, short, sentence"
character = ','
def splitSentence(sentence,character):
    '''Splits a sentence by defined character and prints it'''
    print(sentence.split(character))

splitSentence(sentence,character)