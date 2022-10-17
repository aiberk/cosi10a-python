# Boiling Point
import math
def boiling_point(altitude_input):
    '''Function that calculates boiling points relative to altitude.'''
    altbase = 1 - 0.0000068753*altitude_input
    pressure = 29.921*altbase**5.2559 
    bp = math.floor(49.161* math.log(pressure) + 44.932)
    print(bp)

boiling_point(20)
