def gets_B(score):
    '''returns True if a person gets a B'''
    if score>=80 and score<90:
        return True
    else:
        return False
print(gets_B(50))
print(gets_B(86))
print(gets_B(80))
print(gets_B(100))