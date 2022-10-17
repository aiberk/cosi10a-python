# write a function euro-date(x)
# which converts a string x representing a us date (e.g. "05/21/2022")
# into a European format (e.g. "21.05.2022"

# I'll start:

# def euro-date(x):
#     ''' converts us dates to european format '''

# call like this
# > euro-date("05/21/2022")
# "21.05.2022"


def euroDate(date):
    ''' converts us dates to european format '''
    withOutSlash= date.split('/')
    result = withOutSlash[1]+'.'+withOutSlash[0]+'.'+withOutSlash[2]
    print(result)
    
date ="05/15/2022"
euroDate(date)