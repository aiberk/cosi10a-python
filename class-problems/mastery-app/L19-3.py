# write the code to print out the courses with at least 200 enrolled students!
# in that 4 year period ...
# Just print the subject, coursenum, title, term, and instructor

import csv
with open('courses-2014-19.tsv') as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:
        if((line[8])=="enrolled"):
            continue
        elif(int(line[8])>=200):
            print("Subject:",line[0],"Course Number:",line[1],"Title:",line[3],"Term:",line[6],"Instructor:",line[5])


# import csv
# with open('courses-2014-19.tsv') as file:
#     tsv_file = csv.reader(file, delimiter="\t")
#     for line in tsv_file:
#         if(type(line[8])=="enrolled"):
#             continue
#         elif(int(line[8])>=200):
#             print("Subject:",line[0],"Course Number:",line[1],"Title:",line[3],"Term:",line[6],"Instructor:",line[5])


# import csv
# cfile = open('L19/coursedemo/courses-2014-19.tsv','r')
# reader = csv.DictReader(cfile,delimiter='\t')
# courses = list(reader)
# print(len(courses))

# c = courses[1000]
# print(c)

# #print out Tim's courses
# for course in courses:
# if course["enrolled"]>200:
# print(course['title'],course['term'],course['subject'],course['instructor'],course['coursenum'])