# #modify this code to find the average size of COSI courses ..... course['subject']=='COSI'
# def avg_COSI_class_size(courses):
#     total = 0
#     counter = 0
#     for course in courses:
#         enrolled = int(course['enrolled'])
#         if enrolled>0:
#             total = total + enrolled
#             counter = counter+1
#     return total/counter

# print('avg class size is',avg_class_size(courses))
'''
Load All Brandeis courses from
Fall 2014 to Spr 2019 as a list of dictionaries
'''

import csv
import math

infile = open("courses-2014-19.tsv","r")
reader = csv.DictReader(infile,delimiter='\t')
courses = list(reader)

def avg_subject_class(list, subject):
    '''Gets a file of of classes and returns the average size in a COSI class '''
    total_cosi_classes = 0
    total_cosi_students = 0
    for item in list:
        if(item['subject']== subject):
            total_cosi_classes += 1
            total_cosi_students = total_cosi_students + int(item['enrolled'])
    average = total_cosi_students/total_cosi_classes
    print("Average number of students in",subject,"classes is", str(math.floor(average)))
    return average

avg_subject_class(courses,'COSI')
avg_subject_class(courses,'BIOL')











# import pandas as pd
# interviews_df = pd.read_csv('courses-2014-19.tsv', sep='\t')
 
# # printing data
# print(interviews_df)

# def avg_COSI_class_size(courses):
#     total = 0
#     counter = 0
#     for course in courses:
#         enrolled = int(course['enrolled'])
#         if enrolled>0:
#             total = total + enrolled
#             counter = counter+1
#     return total/counter

# print('avg class size is',avg_class_size(courses))