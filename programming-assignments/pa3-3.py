# You are to write a program to play the game NIM against a user, as described below.

# You should solve this problem by writing a sequence of programs nim0.py, nim1.py, nim2.py, nim3.py, etc.
# following a top-down development style as shown in class, where each one is an extension of the previous one 
# that gets closer to the final product by defining and using new functions.

# What to submit:
# Submit all of the versions below, separated by lines of dashes '--------------------------------------------------'
# Also include a sample of game play for your final version.

# NIM is a game that starts with three positive numbers: a, b, and c
# Let's represent it by a dictionary nim_state={a:10, b:10, c:10}
# At each step a play picks a number (a, b, or c) and removes 1 or more from that number, possibly all.
# The loser is the person who takes the last number from the last peg.
# Your computer player can just randomly pick a number (a,b,c) which is not zero
# and then randomly pick some value to subtract from it (at least 1).

# Here is a link to a wikipedia article about NIM which also describes a winning strategy
# https://en.wikipedia.org/wiki/Nim
# If you want to implement the winning strategy you may, but you only need to implement
# the random strategy as described above for this assignment.

# Here is a sample of play. Your program should produce "identical" output, although the moves of course will be different.
# --------------------------------------------
# Let's play NIM!
# NIM_State {a:10, b:10, c:10}

# your move:  b 10
# removing 10 from b gives
# NIM State {a:10, b:0, c:10}

# computer move: c 5
# removing 5 from c gives
# NIM State {a:10, b:0, c:5}

# your move:  c 5
# removing 5 from c gives
# NIM State {a:10, b:0, c:0}

# computer move: a 8
# removing 8 from a gives
# NIM State {a:2, b:0, c:0}

# your move:  a 1
# removing 1 from a gives
# NIM State {a:1, b:0, c:0}

# computer move: a 1
# removing 1 from a gives
# NIM State {a:0, b:0, c:0}

# --------------------------------------------
# # Note that the user move is a string consisting of a letter a,b,or c  followed by some white space, and a number
