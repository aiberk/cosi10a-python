# modify the code below to define 

# avg_class_size_by_subject(courses,subject)

# import csv

# infile = open('courses-2014-19.tsv','r')
# reader = csv.DictReader(infile,delimiter='\t')
# courses = list(reader)

# print(len(courses))
# c1000 = courses[1000]
# print(c1000)
# for key in c1000:
#     print(key,c1000[key])

# def avg_class_size(courses):
#     total = 0
#     counter = 0
#     for course in courses:
#         enrolled = int(course['enrolled'])
#         if enrolled>0:
#             total = total + enrolled
#             counter = counter+1
#     return total/counter

# print('avg class size is',avg_class_size(courses))

# def courses_by_subject(courses,subject):
#     ''' returns a list of all courses
#         in that subject '''
#     courselist = []
#     for course in courses:
#         if course['subject']==subject:
#             courselist.append(course)
#     return courselist

# avgCOSIsize = avg_class_size(courses_by_subject(courses,'COSI'))
# avgECONsize = avg_class_size(courses_by_subject(courses,'ECON'))
# print(avgCOSIsize,'CS')
# print(avgECONsize,'ECON')