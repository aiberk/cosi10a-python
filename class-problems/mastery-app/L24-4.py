# write the python code to define the sorted list cs_instr_s19 of COSI instructors from Spring 2019
'''
Scripts for practicing working with lists, sets, tuples, and dictionaries
'''

import csv
temp =[]
to_sort = []
with open('L24/courses-2014-19.tsv','r',encoding='utf-8') as tsvfile:
    courses = list(csv.DictReader(tsvfile,delimiter='\t'))
    for items in courses:
        temp.append([items['instructor'],items['subject']])
x=0        
for items in temp:
    if(items[x][1]=='COSI'):
        print(items)
        x = x+1

# subject = sorted({c['instructor'] for c in courses})
# print(temp[0][1])


# instructor = sorted({c['instructor'] for c in courses})
# print(len(instructor))
# print(instructor[0:5])

