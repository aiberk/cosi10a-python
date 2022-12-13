# Now that we know we have a DNA molecule, we need to unzip that gene! DNA helicase works by finding a specific location in 
# the genome, and separating the strand, allowing a polyermase to bind to that spot in the genome. Write a function, helicase, 
# that acts like a helicase! Write a function unzip, which given a string and a start bp, return the part of the gene from that 
# start location to the end of the strand.
# For example, unzip("ATCCCCGA", 2) would give you "CCCCGA"

def unzip(dna_string, start_bp):
    '''Receives a string and a index to unzip the dna molecule'''
    dna_list = [*dna_string]
    new_list =[]
    for index, letter in enumerate(dna_list):
        if(index>start_bp-1):
            new_list.append(letter)
    return "".join(new_list)

print(unzip("ATCCCCGA", 2))
print(unzip('TTTACACCATAGTCGGTGCT', 4))