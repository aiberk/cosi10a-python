'''
adventure game - guess numbers for points and health
This is a demo to show how dictionaries can be used to 
maintain the state of an interactive app.
'''
from random import randint


def print_state(state):
    ''' show values of state variables '''
    print('-'*20)
    print("You are in the",state['room'],
            '.  STATUS: points:',state['points'],
            'health:',state['health'])
    print()



def play_game(state):
    ''' move to the appropriate room and check for win or loss '''
    while state['room']!= 'exit':
        print_state(state)

        #refactor the next code segment into a function
        room = state['room']
        if room=='entry':
            process_entry(state)
        elif room=='kitchen':
            process_kitchen (state)
        elif room=='dining room':
            process_dining_room(state)
        elif room=='exit':
            print('goodbye!')
        
        # refactor the next code segment into a function
        if state['health']<=0 or state['points']<=0:
            print('you lose!')
            state['room'] = 'exit'
        if state['points']>=100:
            print('you win!')
            state['room']=='exit'

def process_entry(state):
    ''' play guessing game and possibly move to kitchen '''
    print('Welcome to the guessing game room')
    play_guessing_game(state)
    response = input("Do you want to eat? (y or n): ")
    if response=='y':
        state['room']= 'kitchen'

def play_guessing_game(state):
    ''' ask user to guess a number and reward or penalize accordingly '''
    answer = randint(1,4)
    guess = int(input("guess a number between 1 and 4 to get 20 points: "))
    if guess==answer:
        print("You guessed it. You get 20 points!")
        state['points'] += 20
    else:
        print("Wrong guess. The answer was",answer)
        print("You lose 10 points")
        state['points'] -= 10

def process_kitchen(state):
    ''' let user buy some food and change points/health '''
    print("What do you want to eat?")
    response = input("steak salad sushi or nothing: ")
    if response=='steak':
        state['points'] -= 20
    elif response=='salad':
        state['points'] -= 5
    elif response=='sushi':
        state['points'] -= 20
    
    if response=='nothing':
        state['health'] -= 5
        state['room']= 'entry'
    else:
        state['health'] += 10
        state['room'] = 'dining room'

def process_dining_room(state):
    ''' kick user out if they don't like the food '''
    response = input("is your meal good? (y or n): ")
    if response=='y':
        state['room']='entry'
    else:
        print("You are ungrateful and I'm kicking you out!")
        print("Goodbye!")
        state['room']='exit'

starting_state = {'room':'entry','points':100,'health':10}

play_game(starting_state)
