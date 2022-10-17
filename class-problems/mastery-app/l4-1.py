# Complete the following change program so it says how many quarters (25) ,
#  dimes (10), nickels(5) , and pennies(1) you get back in change.

# '''
# change.py is a script to calculate change
# '''
# n = int(input("How much change do you have? "))
# print('converting',n,"into change gives")
# quarters = n//25
# print(quarters,'quarters and')
# n = n% 25   #  this is how much we have left to change
# print('????',n)


n = int(input("How much change do you have? (in cents) "))
quarters = n//25
dimes = (n-(quarters*25))//10
nickels = (n-(quarters*25)-(dimes*10))//5
pennies = (n-(quarters*25)-(dimes*10)-(nickels*5))//1
print('converting',n,"cents into change gives",quarters,"quarters",dimes,"dimes",nickels,"nickels",pennies,"pennies")

