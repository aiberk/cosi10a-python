# Write a script to convert temperatures from Farenheit to Centigrade.
# subtract 32 and multiply by 5/9 to get C from F
#   (use input to get values and print to show result), e.g.

# enter temp in F:  212
# temp in C is 100


def farenheit2celsius():
    input_temperature = int(input("Enter temp in F:"))
    result = (input_temperature-32)*(5/9)
    print("Temp in C is",result)
farenheit2celsius()