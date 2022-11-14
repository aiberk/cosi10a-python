# ## Dictionary items cannot be edited - so they are copied, the new copy is added to the object and the OG one deleted.


# The file RE.csv which you can get from this URL
#         https://www.cs.brandeis.edu/~tim/cs10afall22/
# contains information about homes sales in California about 15 years ago.
# You can read it in using csv.DictReader and you will get a list of dictionaries of the following form:

# {'street': '12209 CONSERVANCY WAY', 
# 'city': 'RANCHO CORDOVA', 
# 'zip': '95742', 
# 'state': 'CA', 
# 'beds': '0', 
# 'baths': '0', 
# 'sq__ft': '0', 
# 'type': 'Residential', 
# 'sale_date': 'Wed May 21 00:00:00 EDT 2008', 
# 'price': '263500', 
# 'latitude': '38.553867', 
# 'longitude': '-121.219141'}

# Your goal is to write a Python script which asks the user how much is the most they can afford and then prints the price, sq__ft, and city for all homes under that price where the square feet is > 0 (some list the square feet as 0 and that is just missing data, so ignore it!)

# Here is the sample output your program should produce:

# What is the most you can spend? 50000
# price: 40000 sq__ft 840 city SACRAMENTO
# price: 48000 sq__ft 484 city SACRAMENTO
# price: 30000 sq__ft 1166 city CITRUS HEIGHTS
# price: 2000 sq__ft 5822 city SLOUGHHOUSE
# continue? (y or n) y
# What is the most you can spend? 60000
# price: 59222 sq__ft 836 city SACRAMENTO
# price: 40000 sq__ft 840 city SACRAMENTO
# price: 48000 sq__ft 484 city SACRAMENTO
# price: 30000 sq__ft 1166 city CITRUS HEIGHTS
# price: 55422 sq__ft 838 city SACRAMENTO
# price: 2000 sq__ft 5822 city SLOUGHHOUSE
# price: 56950 sq__ft 1512 city SACRAMENTO
# continue? (y or n) n

# It looks like the SLOUGHHOUSE  data is probably wrong unless it is a real "fixer-uppper"

import csv

def find_by_price():
# opening the CSV file
    with open('RE.csv', mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.DictReader(file)
       user_input_amount = int(input('What is the most you can spend?\n'))
       # displaying the contents of the CSV file
       for key in csvFile:
            if(int(key['price'])<=user_input_amount):
                print('price:',key['price'],'sq__ft:',key['sq__ft'],'city',key['city'])
       
       
            user_input_continue = input('What is the most you can spend?\n')
            if(user_input_continue == 'Y'):
                find_by_price()
            elif(user_input_continue=='N'):
                exit()

find_by_price()
