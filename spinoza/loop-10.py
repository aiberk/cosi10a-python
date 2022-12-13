# DNA has very specific base pairing rules. A with T, C with G. Take our DNA strand and write a function, translate, 
# that returns a new string with the translation.

# For example, translate("ATTGC") would return "TAACG", where the A's get translated to T's
#  (and vice versa), and the G's get translated to C's (and vice versa)

def translate(dna_string):
    '''Translates DNA string, A <-> T and C <-> G'''
    new_string =''
    print(dna_string)
    for letter in dna_string:
        if letter == 'A':
            new_string = new_string + 'T'
        elif letter == 'T':
            new_string = new_string + 'A'
        elif letter == 'C':
            new_string = new_string + 'G'
        elif letter == 'G':
            new_string = new_string + 'C'
    return new_string