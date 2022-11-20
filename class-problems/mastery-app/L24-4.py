# write the python code to define the sorted list cs_instr_s19 of COSI instructors from Spring 2019
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