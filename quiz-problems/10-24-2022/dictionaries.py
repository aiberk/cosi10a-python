# For this problem we will use the csv file courses-2014-19.tsv which is in tab-separated-values format
# and can be accessed from this website:
# https://www.cs.brandeis.edu/~tim/cs10afall22/
# This file represents courses at Brandeis and was used in class last Wednesday.
  
# The first few lines of the file are:

# subject	coursenum	section	title	format	instructor	term	code	enrolled
# AAAS	5A	1	INTRO AFR./AFR0-AM STUDY	LEC	"Williams, Chad"	Fall 2018	1183	21
# AAAS	5A	1	INTRO AFR./AFR0-AM STUDY	LEC	"Smith, Faith"	Fall 2017	1173	29

# Write a Python script which reads this into a list of dictionaries (using csv.DictReader). For example, the second row will be stored in a dictionary of the following form:
# {'subject': 'AAAS', 'coursenum': '5A', 'section': '1', 'title': 'INTRO AFR./AFR0-AM STUDY', 'format': 'LEC', 'instructor': 'Smith, Faith', 'term': 'Fall 2017', 'code': '1173', 'enrolled': '29'}

# It should then have a loop where it asks the user for an instructors name and then calculates
# * the total number of courses taught by that instructor with at least 8 students
# * the total number of students taught in such courses
# * the average course size
# It will then ask if they want to continue and will repeat until they are done.

# Your program output should look like the following:

# Enter the name of an instructor in the form Last, First: Hickey, Timothy
# Hickey, Timothy taught 26 courses with at least 8 students
# they taught 1831 students total (with double counting)
# their average class size was 70.42307692307692
# continue with another instructor? y

# Enter the name of an instructor in the form Last, First: Salas, R. Pito     
# Salas, R. Pito taught 27 courses with at least 8 students
# they taught 867 students total (with double counting)
# their average class size was 32.111111111111114
# continue with another instructor? n

# bye

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
    print("Average number of students in",subject,"classes is", str(average))
    return average

avg_subject_class(courses,'COSI')
avg_subject_class(courses,'BIOL')