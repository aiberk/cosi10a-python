# write the python code to print all words of 
# length 20 or more in the word list


'''
crossword helper
'''
targetWordsList=[]
wordfile = open('10000.txt','r')
wordstring = wordfile.read()
words = wordstring.split()
for word in words:
    if(len(word)>=20):
        targetWordsList.append(word)
print(targetWordsList)
print('There are',len(targetWordsList),'words')

