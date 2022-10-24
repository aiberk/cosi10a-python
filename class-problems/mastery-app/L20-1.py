# write a function:
# avg_weight(pets)
# which returns the average weight of the pets in the list ...
pets = [
{'name':"Pippin", 'species':'dog',  'age':18, 'weight':8, 'personality':'chill'},
{"name":"bonzo",  'species':"frog", 'age': 2, "weight":2, 'personality':'funny'},
{'name':'George', 'species':'dog',  'age': 2, 'weight':25, 'personality': 'cuddly'},
{'name':'Leo',    'species':'dog',  'age': 1, 'weight':18,'personality':'happy'}
]
def avg_wieghts(list):
    sum = 0
    for item in list:
        sum = sum + item["weight"]
    average = sum/len(list)
    return average
print(avg_wieghts(pets))
    