# given a string d representing a date, e.g. x ="05/15/2022"
# write expression to get the month m, the day d, and the year y

# e.g.  m = x[:2]
monthName = ["NOM","January","February","March","April","May","June","July","August","September","October","November","December"]
date ="05/15/2022"
def formatDate(date):
    '''Gets a date in MM/DD/YYYY and turns it into Month Day Year'''
    result = ''
    space = " "
    withOutSlash= date.split('/')
    result = str(monthName[int(withOutSlash[0])]) + space +  str(int(withOutSlash[1])) + "th" + space+ str(int(withOutSlash[2]))
    print(result)

    
formatDate(date)