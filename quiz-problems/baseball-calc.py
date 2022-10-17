#prompt user for velocity and angle
#use formula to calculate height
import math
print('')
velocity_input = float(input("What is the velocity?"))
angle = float(input("What is the angle?"))
velocity = velocity_input/3600*5280
vertical_velocity = velocity_input*(math.sin(math.pi*(angle/180)))
time = vertical_velocity/32
height = -16*(time**2)+(vertical_velocity*time)

print('')
print('Baseball height calculator')
print('--------------------------')
print('Initial velocity', velocity, 'mph')
print('Initial angle', angle,'deg')
print('Peak reached at:', time, 'seconds')
print('Peak height:', height)
