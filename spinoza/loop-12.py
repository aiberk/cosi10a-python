# The temperature that DNA should be amplified at can be approximated by using the formula:

# Temp(in celcuis) = 81.5 + 0.41(%GC) - (675/N)
# Where %GC is the percent of the base pairs that are a G's or C's
# and N is the total number of base pairs.

# Write the function annealing_temp which takes a DNA string, and approximates the temperature that it should be amplified at.

# For example, annealing_temp("ATGCATGCATGCATGCATGC") would return 81.5 + .41(.50) - (675/20) = 47.955