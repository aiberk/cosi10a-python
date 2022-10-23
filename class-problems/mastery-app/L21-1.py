# Modify the process_entry code
# so that it ask if they want to go to work?
# if they say yes, it sets the 'room' to 'office'

# and modify the play_game so that if room is 'office'
# it says time to go home and adds 50 points to the dictionary
# and sets room to entry...

# def process_entry(state):
#     ''' play guessing game and possibly move to kitchen '''
#     print('Welcome to the guessing game room')
#     play_guessing_game(state)
#     response = input("Do you want to eat? (y or n): ")
#     if response=='y':
#         state['room']= 'kitchen'



# def play_game(state):
#     ''' move to the appropriate room and check for win or loss '''
#     while state['room']!= 'exit':
#         print_state(state)

#         #refactor the next code segment into a function
#         room = state['room']
#         if room=='entry':
#             process_entry(state)
#         elif room=='kitchen':
#             process_kitchen (state)
#         elif room=='dining room':
#             process_dining_room(state)
#         elif room=='exit':
#             print('goodbye!')
        
#         # refactor the next code segment into a function
#         if state['health']<=0 or state['points']<=0:
#             print('you lose!')
#             state['room'] = 'exit'
#         if state['points']>=100:
#             print('you win!')
#             state['room']=='exit'