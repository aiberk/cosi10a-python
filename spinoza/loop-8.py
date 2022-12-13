# Write a function count_base_pairs, that takes a string of DNA (containing only the characters "A", "C", "G", "T"), 
# and return a list of 4 numbers, how many A's, C's, G's, and T's are in the string (in that order).

# For example, count_base_pairs("ACCGCA") would return the list [2, 3, 1, 0], since there are 2 A's, 3 C's, 1 G, and 0 T's. 

def count_base_pairs(dna_string):
    '''Counts Base Pairs in a DNA sequence and returns an array with occurences of A,C,G,T in that order'''
    a_count = 0
    g_count = 0
    c_count = 0
    t_count = 0
    for letter in dna_string:
        if letter == 'A':
            a_count = a_count + 1
        elif letter == 'C':
            c_count = c_count +1
        elif letter == 'G':
            g_count = g_count +1
        elif letter == 'T':
            t_count = t_count +1
    return [a_count,c_count,g_count,t_count]

print(count_base_pairs("ACCGCA"))