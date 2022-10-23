# Refactor the two if's at the end of the play_game method.
# So think of good function names, and replace the if's with function calls.
# and write  the functions (don't forget the docstring)

# def play_game(state):
#     ''' move to the appropriate room and check for win or loss '''
#     while state['room']!= 'exit':
#         print_state(state)
#         process_next_room(state)
    
#         # refactor the next code segment into a function
#         if state['health']<=0 or state['points']<=0:
#             print('you lose!')
#             state['room'] = 'exit'
#         elif state['points']>=100:
#             print('you win!')
#             state['room']=='exit'

# def process_next_room(state):
#     ''' looks at state['room'] and calls appropriate function '''
#     #refactor the next code segment into a function
#     room = state['room']
#     if room=='entry':
#         process_entry(state)
#     elif room=='kitchen':
#         process_kitchen (state)
#     elif room=='dining room':
#         process_dining_room(state)
#     elif room == 'office':
#         process_office(state)
#     elif room=='exit':
#         print('goodbye!')