# Find the volume of a sphere of radius 5 inches, in cubic inches ..
# Write the Python code you need to calculate this value...

#V = 4/3 πr³
# Import math Library
import math
# Print the value of pi
pi = math.pi
radius = 5
volume = (4/3)*pi*radius**3
print(volume)



# Write the Python code to find out the monthly payment of a $40000 loan
#  at 6% interest for 60 months...

loan = 40000
rate= 0.6 
time = 60
monthly_payment = 12

# ƥ = rP / n * [1-(1+r/n)-nt]
amortization = (rate*loan)/monthly_payment *(1-(1+rate/monthly_payment)**-(monthly_payment*time))
interest = monthly_payment*amortization*time-loan
print(amortization)
print(interest)