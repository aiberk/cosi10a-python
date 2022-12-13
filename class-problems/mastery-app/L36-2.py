# Write the code to create a 10x10 board with 12 mines
# Here is the starter code



# Write a function is_mine(r,c) which returns True if there is a mine (i.e. -2) at row r and col c,
# ie board[r][c]==-2, but ... make sure you first check that r and c are range....
# r in range(len(board))
'''
minesweeper functions for 
representing the board as a list of lists
and the contents of the list represent the users guesses
and the mines ....
So we can start it by specifying the size of the game
and the number of mines...

For the starting board with no mines, we'll put -1 in every position
meaning there is no mine there and the user didn't select that
position.

'''

from random import randint

def make_board(n):
    ''' create a board of size n 
        make_board(3) => [[-1,-1,-1],
                          [-1,-1,-1],
                          [-1,-1,-1]]
    '''
    board = []
    for i in range(n):
        board.append(make_row(n))
    return board


def make_row(n):
    ''' create a list of n -1's 
        make_row(3) -> [-1,-1,-1]
    '''
    return [-1]*n
    # return [-1 for i in range(n)]
    # row=[]
    # for i in range(n):
    #    row.append(-1)
    # return row

def print_board(board):
    ''' print the rows with a space for -1
        print out the values of the board with 2digits and space between
        print("%2d "%(val))
    '''
    for row in board:
        for col in row:
            print("%2d "%(col),end="")
        print()


def place_mines(n,board):
    ''' add up to n -2's into random locations on the board '''
    for i in range(n):
        row = randint(0,len(board)-1)
        col = randint(0,len(board)-1)
        board[row][col]=-2

def is_mine(r,c,board):
    '''Checks if mine exists at row r and column c'''
    if(r in range(len(board)) and c in range(len(board))):
       if(board[r][c]==-2):
        return True
       else:
        return False
    else:
        print("Not in range")



b = make_board(10)
print_board(b)
print('-'*40)
place_mines(12,b)
print_board(b)
is_mine(5,1,b)
