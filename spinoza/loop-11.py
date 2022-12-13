# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# To translate a DNA string to an RNA string, you must replace all of the T's in the DNA with a "U"

# Write a method, dna_to_rna, which takes a dna string and returns the RNA translation.

# For example, dna_to_rna("ATCGC") would return "AUCGC"

def dna_to_rna(rna_string):
    '''Translates DNA string to RNA, T -> U '''
    new_string =''
    for letter in rna_string:
        if letter == 'T':
            new_string = new_string + 'U'
        else:
            new_string = new_string + letter
    return new_string

print(dna_to_rna('ATCGCTTTUUUGCTGSTDUCTTTTT'))