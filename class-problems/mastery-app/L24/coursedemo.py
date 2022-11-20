'''
Scripts for practicing working with lists, sets, tuples, and dictionaries
'''

# first we read the course data in a list of dictionaries
import csv
with open('courses-2014-19.tsv','r',encoding='utf-8') as tsvfile:
    courses = list(csv.DictReader(tsvfile,delimiter='\t'))

print('there are',len(courses),'courses')

print(courses[12345])
c12345 = courses[12345]
for key in c12345:
    print(key,':',c12345[key])

terms = sorted({c['term']  for c in courses})
print(terms)