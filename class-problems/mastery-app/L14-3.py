# Write the python code to print out all five letter words
#  where the 2nd letter is 't' and the last letter is 'e'
# Hint: use a for loop to go through all the words, check 
# if the conditions are met, and print if so ...

'''
crossword helper
'''
import re
targetWordsList=[]
wordfile = open('10000.txt','r')
wordstring = wordfile.read()
words = wordstring.split()
for word in words:
    x = re.findall("^.{1}t.*e", word)
    if(x):
        targetWordsList.append(x)

print(targetWordsList)
print('There are',len(targetWordsList),'words')

