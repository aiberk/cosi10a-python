# Modify the code below to ask the user how much they want to bet in each round
# and then adjust the balance according to if they win or lose...

# def play_craps():
#     ''' repeatedly asks the user if they want to play
#         if so, it calls play1game()
#         and continues until they don't want to play anymore
#     '''
#     balance=100
#     print('you have',balance,'dollars')
#     playvar = input("Do you want to play a game of craps? (y/n) ")
#     while playvar == "y":
#         user_won = play1game()
#         if user_won:
#             print('good job, you won')
#         else:
#             print('sorry you lost')
#         print('you have',balance,'dollars')
#         playvar = input("Do you want to play again? (y/n)")
#     print('Goodbye')