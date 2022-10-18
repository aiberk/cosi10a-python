# Modify the code so that it doesn't let the user bet more than their balance!
# (Hint: use continue to skip the rest of the loop and start the body again)

# def play_craps():
#     ''' repeatedly asks the user if they want to play
#         if so, it calls play1game()
#         and continues until they don't want to play anymore
#     '''
#     balance=100
#     print('you have',balance,'dollars')
#     playvar = input("Do you want to play a game of craps? (y/n) ")
    
#     while playvar == "y":
#         bet = int(input("how much do you want to bet?"))
#         user_won = play1game()
#         if user_won:
#             print('good job, you won')
#             balance+=bet
#         else:
#             print('sorry you lost')
#             balance-=bet
#         print('you have',balance,'dollars')
#         playvar = input("Do you want to play again? (y/n)")
#     print('Goodbye')