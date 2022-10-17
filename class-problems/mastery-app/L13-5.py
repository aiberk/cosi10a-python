# Modify the code below to find and print all words starting with z and ending with g

# for w in vals:
#     if w[0]=='q':
#         print(w)
import re
words = ["hello",'zellog','zello','hellog']
for word in words:
    x = re.findall("z.*g", word)
    if(x):
        print(x)