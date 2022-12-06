# ou are to write a Python script which reads in the file baby100.csv from this URL
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

# Your script should ask for a rank (from 1 to 100)
# and it should return the set of all tuples (name,sex) for which 
# the baby name/sex had the specified rank for some year.

# Here is what your output should look like:
# rank: 1
# sex (M or F): M
# ('Noah', 'M')
# ('John', 'M')
# ('David', 'M')
# ('Michael', 'M')
# ('Robert', 'M')
# ('Liam', 'M')
# ('James', 'M')
# ('Jacob', 'M')
# more? (y or n) y
# rank: 1
# sex (M or F): F
# ('Mary', 'F')
# ('Emily', 'F')
# ('Isabella', 'F')
# ('Jennifer', 'F')
# ('Sophia', 'F')
# ('Linda', 'F')
# ('Jessica', 'F')
# ('Ashley', 'F')
# ('Olivia', 'F')
# ('Lisa', 'F')
# ('Emma', 'F')
# more? (y or n) n


import csv

def find_by_rank_in_csv():
    '''Finds name and sexes by rank'''
    return_value =[]
    with open('baby100.csv', mode ='r') as file: 
        csvFile = csv.DictReader(file)
        user_input_rank = input('Enter a rank:\n')
        for row in csvFile:
                if(row['rank']==user_input_rank):
                    return_value.append((row['name'],row['sex']))
        for rows in return_value:
            print(rows)


def find_by_rank():
    '''Finds name and sexes by rank'''
user_is_active = True
while(user_is_active):
            find_by_rank_in_csv()
            user_input_continue = input('Continue? (Y or N)')
            if(user_input_continue == 'Y' or user_input_continue == 'Yes' or user_input_continue == 'y' or user_input_continue == 'yes'):
                find_by_rank()
            elif(user_input_continue=='N' or user_input_continue=='No' or user_input_continue=='n' or user_input_continue=='no'):
                quit()



find_by_rank()