import math
def cylinder_volume():
    '''Takes in a height and radius, calculates volumes, and returns a float'''
    height = float(input('What is the height?'))
    radius = float(input('What is the radius?'))
    print('Volume:')
    print((math.pi*(radius**2))*height)

def sphere_volume():
    '''Takes in a radius, calculates volumes, and returns a float'''
    radius = float(input('What is the radius?'))
    print('Volume:')
    print((4/3)*(math.pi*(radius**3)))


sphere_volume()
cylinder_volume()