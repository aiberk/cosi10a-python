# You are to write a Python script which reads in the file baby100.csv from this URL
#    https://www.cs.brandeis.edu/~tim/cs10afall22
# This contains information about the top 100 boys and girls baby names from 1880 to 2019
# The first and last few lines of the file are as follows:
# year,name,sex,count,percent,rank
# 1880,Mary,F,7065,0.035064819042703144,1
# 1880,Anna,F,2604,0.012924103154592921,2
# 1880,Emma,F,2003,0.009941236028667288,3
# ...
# 2019,Kayden,M,3887,0.0011281967630882579,97
# 2019,Parker,M,3878,0.001125584524635005,98
# 2019,Wesley,M,3731,0.001082917963231873,99
# 2019,Kai,M,3718,0.0010791447299105077,100

# Your script should repeatedly ask the user for name and a sex (M or F) and then print out the tuples (count,year)
# sorted from largest to smallest.

# Here is an example of the output of your script:
# Enter a name: Whitney
# Enter a sex: (M or F) F
# (9536, '1986')
# (8920, '1987')
# (7852, '1988')
# (6307, '1989')
# (5904, '1990')
# (5240, '1991')
# (4077, '1993')
# (4010, '1992')
# (3833, '1985')
# (3566, '1994')
# more? (y or n) n




import csv

def find_by_name_and_sex():
    '''Finds the count and year of a name and sex'''   
    user_is_active = True
    while(user_is_active):
            print(check_csv())
            user_input_continue = input('Continue? (Y or N)')
            if(user_input_continue == 'Y' or user_input_continue == 'Yes' or user_input_continue == 'y' or user_input_continue == 'yes'):
                find_by_name_and_sex()
            elif(user_input_continue=='N' or user_input_continue=='No' or user_input_continue=='n' or user_input_continue=='no'):
                quit()

def check_csv():
    '''Opens csv and filters the csv, finally prints what is selected'''
    return_value =[]
    with open('baby100.csv', mode ='r') as file: 
        csvFile = csv.DictReader(file)
        user_input_name = input('Enter a name:\n')
        user_input_sex = input('Enter a sex: (M or F)\n')
        for row in csvFile:
            if(row['name']==user_input_name and row['sex']==user_input_sex ):
                return_value.append((row['count'],row['year']))
        for rows in return_value:
            print(rows)
    

            
find_by_name_and_sex()

