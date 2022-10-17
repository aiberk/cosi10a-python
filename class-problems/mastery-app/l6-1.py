# Write a function years2billionseconds which converts years into billions of seconds.
# It should call years2minutes to do the calculation..

# Expand on this code:
# def years2days(years):
#     "convert years to days"
#     days = years*365.25
#     return days

# def years2minutes(years):
#     "convert years to minutes"
#     days = years2days(years)
#     minutes = days*24*60
#     return minutes

def years2days(years):
    "convert years to days"
    days = years*365.25
    return days

def years2minutes(years):
    "convert years to minutes"
    days = years2days(years)
    minutes = days*24*60
    return minutes

def years2billionseconds(years):
    "convert years to minutes"
    minutes = years2minutes(years)
    billionsOfSeconds = minutes*60*1000000000
    return billionsOfSeconds

print(years2billionseconds(10),"billions of seconds")