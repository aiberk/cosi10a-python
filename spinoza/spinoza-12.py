# Write a method years2minutes(years) which converts a number of years into minutes by multiplying the 
# number of years by 365.25 days in a year, 
# 24 hours in a day, and 60 minutes in an hour

def years2minutes(years):
    '''converts a number of years into minutes by multiplying the number of years by 365.25 days in a year, 
    24 hours in a day, and 60 minutes in an hour'''
    return ((((years*365.25)*24)*60))

print(years2minutes(1))