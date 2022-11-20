# write the python code to create a sorted list of the instructors of courses 
# and print the length of that list  and  print the first 5 elements

'''
Scripts for practicing working with lists, sets, tuples, and dictionaries
'''

# first we read the course data in a list of dictionaries
import csv
with open('L24/courses-2014-19.tsv','r',encoding='utf-8') as tsvfile:
    courses = list(csv.DictReader(tsvfile,delimiter='\t'))
instructor_list = []
for lines in courses:
    instructor_list.append(lines['instructor'])
sorted_instructor_list = sorted(instructor_list)
x=5
while(x>=0):
    print(f'Instructor {x} is {sorted_instructor_list[x]}')
    x = x-1

print(len(sorted_instructor_list))

# instructor = sorted({c['instructor'] for c in courses})
# print(len(instructor))
# print(instructor[0:5])