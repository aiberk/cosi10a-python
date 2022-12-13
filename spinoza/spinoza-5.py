# write a method triangleArea(a,b,c)
# which returns the area of a triangle whose three sides have length a,b, and c.

# You should use Heron's formula which is
# area = sqrt(s(s-a)(s-b)(s-c))
# where s=(a+b+c)/2
import math

def triangleArea(a,b,c):
    '''returns the area of a triangle whose three sides have length a,b, and c'''
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
   

print(triangleArea(30,30,30))