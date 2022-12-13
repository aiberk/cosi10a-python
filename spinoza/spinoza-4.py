# Write the function, mph2fps(speed) which converts a speed from miles per hour to feet per second.  
# It should multiply the speed by 5280 to get feet per hour, and then divide that by 3600 to get feet per second.

# e.g. 
# mph2fps(60) --> 88  because 60 miles per hour is 88 feet per second
# mph2fps(0) --> 0
# mph2fps(30) --> 44  

def mph2fps(speed):
    '''converts a speed from miles per hour to feet per second'''
    return (speed*5280)/3600

print(mph2fps(60))
print(mph2fps(0))
print(mph2fps(30))
