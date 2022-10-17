# answer the previous problem with negative indices in your slice!
# what is the Python slicing expression to get the list ["it", "needs", "not"] from vals where vals = 
# ['tell', 'me', 'not', 'here', 'it', 'needs', 'not', 'saying']
a = ['tell', 'me', 'not', 'here', 'it', 'needs', 'not', 'saying']
x = slice(-4,7)
print(a[x])