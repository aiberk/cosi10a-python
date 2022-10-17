
last_input = 0
count = 0 
penny_array = []
dime_array = []
nickel_array = []
quarter_array = []
while last_input != 'x':
    last_input = input("More coins?")
    if last_input == 'p':
        penny_array.append('p')
        count = count + 1
    elif last_input == 'n':
        nickel_array.append('n')
        count = count + 5
    elif last_input == 'd':
        dime_array.append('d')
        count = count + 10
    elif last_input == 'q':
        quarter_array.append('q')
        count = count + 25
    else:
        print('Please add correct amount')
    print('You have', count ,'cents so far')
print('The total is ', count ,'cents')
print(len(penny_array), 'pennies for',len(penny_array)*1,'cents')
print(len(nickel_array), 'nickels for',len(nickel_array)*5,'cents')
print(len(dime_array), 'dimes for',len(dime_array)*10,'cents')
print(len(quarter_array), 'quarters for',len(quarter_array)*25,'cents')