# Write a function degToRadian(d) which converts the value d from degrees to radians using the formula  r=d/180*math.pi
# Remember to import the math module...
import math
def degToRadian(d):
    '''Converts degrees to radians using r=d/180*math.pi'''
    return d/180*math.pi
print(degToRadian(360))