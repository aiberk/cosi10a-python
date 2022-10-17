n = int(input("How much change do you have? "))
print('converting',n,"into change gives")
quarters = n//25
print(quarters,'quarters and')
n = n% 25   #  this is how much we have left to change
print('????',n)