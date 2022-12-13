# An arc of a circle is a segment of the circumference of the circle.
# circle graphic


# Write a function called arc_length which takes the angle (in degrees) that the arc encompasses, and the radius of the circle, and returns the length of the arc. 

# This can be computed by the following formula:

# arc length = angle * (pi/180) * radius
import math
def arc_length(angle,radius):
    ''''Computes arc length, with angle and radius'''
    return angle * (math.pi/180) * radius