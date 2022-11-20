
# Write the python code to find the sorted list of subjects of courses  (i.e. key is subject
# print the length of subjects and the last five subjects ..

'''
Scripts for practicing working with lists, sets, tuples, and dictionaries
'''

import csv
with open('L24/courses-2014-19.tsv','r',encoding='utf-8') as tsvfile:
    courses = list(csv.DictReader(tsvfile,delimiter='\t'))
subject = sorted({c['subject'] for c in courses})
length = len(subject)
print(length)
print(subject[0:-5])