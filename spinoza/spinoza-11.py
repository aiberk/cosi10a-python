# Write a function triangle_area(side1, angleD, side2) which calculates the area of a triangle from an angle 
# (in degrees) and the lengths of two sides. You should use this formula
#     angleR = angleD/180*pi
#     area = side1 * side2/(2 * sin(angleR))
import math

def triangle_area(side1, angleD, side2):
    '''which calculates the area of a triangle from an angle 
# (in degrees) and the lengths of two sides'''
    angleR = angleD/180*math.pi
    return side1 * side2/(2 * math.sin(angleR))